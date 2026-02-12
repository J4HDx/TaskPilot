import importlib
from typing import Dict, Any

from .. import schemas
from ..connectors.base import BaseConnector
from ..celery_app import celery_app

def get_connector(connector_name: str) -> BaseConnector:
    """
    Dynamically imports and instantiates a connector from the `connectors` directory.
    """
    try:
        module_path = f"connectors.{connector_name}.connector"
        module = importlib.import_module(module_path, package="backend")
        class_name = f"{connector_name.capitalize()}Connector"
        connector_class = getattr(module, class_name)
        return connector_class()
    except (ImportError, AttributeError) as e:
        print(f"Error loading connector '{connector_name}': {e}")
        raise

@celery_app.task(name="taskpilot.runner.execute_trigger")
def execute_trigger(flow_data: Dict[str, Any]):
    """
    Celery task to execute a single flow's trigger.
    """
    flow = schemas.Flow.model_validate(flow_data)
    print(f"Executing trigger for flow: {flow.name} ({flow.id})")

    try:
        trigger_connector = get_connector(flow.trigger.connector)
        trigger_events = trigger_connector.trigger(
            event=flow.trigger.event,
            event_config=flow.trigger.config
        )

        if trigger_events:
            print(f"Trigger for flow '{flow.name}' found {len(trigger_events)} events.")
            for event_data in trigger_events:
                execute_action.delay(flow_data=flow.model_dump(), event_data=event_data)

    except Exception as e:
        print(f"Error executing trigger for flow {flow.id}: {e}")

@celery_app.task(name="taskpilot.runner.execute_action")
def execute_action(flow_data: Dict[str, Any], event_data: Dict[str, Any]):
    """
    Celery task to execute a flow's action with data from a trigger event.
    """
    flow = schemas.Flow.model_validate(flow_data)
    print(f"Executing action for flow: {flow.name} with event data: {event_data}")

    try:
        action_connector = get_connector(flow.action.connector)
        action_connector.action(
            action=flow.action.action,
            action_config=flow.action.config,
            data=event_data
        )
        print(f"Action for flow '{flow.name}' executed successfully.")

    except Exception as e:
        print(f"Error executing action for flow {flow.id}: {e}")