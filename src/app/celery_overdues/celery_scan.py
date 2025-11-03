from celery_overdues.celery_init import celery
from database import new_session


@celery.task(bind=True, autoretry_for=(Exception,), retry_backoff=True, max_retries=3)
async def scan_and_notify_overdues():
    async with new_session() as session:
        result = session.execute("""
            SELECT *
            FROM tasks
            WHERE status NOT IN ("done", "overdue", "cancelled")
                AND deadline <= NOW()
            RETURNING task_id
        """).fetchall()

        for r in result:
            push_inapp_notification.delay(r.user_id, r.task_id)
