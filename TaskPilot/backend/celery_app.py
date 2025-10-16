from celery import Celery
from .core.config import settings

celery_app = Celery(
    "taskpilot",
    broker=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/0",
    backend=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}/0",
    include=["utils.runner", "utils.scheduler"]
)

celery_app.conf.update(
    task_track_started=True,
    beat_scheduler='django_celery_beat.schedulers:DatabaseScheduler',
)