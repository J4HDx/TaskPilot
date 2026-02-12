from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json

def setup_flow_scheduler():
    """
    Ensures that the periodic task for running the flow scheduler exists.
    This should be called on application startup.
    """
    print("Setting up flow scheduler...")

    # Schedule to run every 30 seconds
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=30,
        period=IntervalSchedule.SECONDS,
    )

    # Create the periodic task to run the main scheduler
    PeriodicTask.objects.get_or_create(
        interval=schedule,
        name='Flow Scheduler',
        task='taskpilot.scheduler.schedule_all_active_flows',
        defaults={'args': json.dumps([])}
    )
    print("Flow scheduler task ensured.")

@celery_app.task(name="taskpilot.scheduler.schedule_all_active_flows")
def schedule_all_active_flows():
    """
    Fetches all active flows from the database and schedules their triggers.
    """
    from .. import models, schemas
    from ..core.database import SessionLocal
    from .runner import execute_trigger

    db = SessionLocal()
    try:
        active_flows = db.query(models.Flow).filter(models.Flow.enabled == True).all()
        print(f"Found {len(active_flows)} active flows.")
        for db_flow in active_flows:
            flow = schemas.Flow.from_orm(db_flow)
            execute_trigger.delay(flow_data=flow.model_dump())
    finally:
        db.close()