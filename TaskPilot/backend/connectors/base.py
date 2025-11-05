from abc import ABC, abstractmethod
from typing import Any, Dict, List

class BaseConnector(ABC):
    """
    Abstract base class for all connectors.

    It defines the interface that every connector must implement to ensure
    consistency and modularity across the platform.
    """

    def __init__(self, config: Dict[str, Any] = {}):
        """
        Initializes the connector with its specific configuration.
        This could include API keys, tokens, or other settings passed from the flow.
        """
        self.config = config

    @abstractmethod
    async def trigger(self, event: str, event_config: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Checks for a specific event and returns data if the event occurred.

        For polling triggers, this method will be called periodically.
        It should return a list of event data, where each item in the list
        will trigger a separate run of the associated action.

        If no event is found, it should return an empty list.
        """
        pass

    @abstractmethod
    async def action(self, action: str, action_config: Dict[str, Any], data: Dict[str, Any]):
        """
        Executes a specific action.

        This method receives the configuration for the action and the data
        payload from the trigger.
        """
        pass