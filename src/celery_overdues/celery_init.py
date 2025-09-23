from celery import Celery

celery = Celery(
    __name__,
    brocker="redis://localhost:6379/0",
    backend="redis://localhost:6379/1",
)

celery.conf.beat_schedule = {
    "scan_overdues_every_minute": {
        "task": "scan_and_notify_overdues",
        "schedule": 60.0,
    }
}