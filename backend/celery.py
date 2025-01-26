from celery import Celery
from celery.schedules import crontab  # To use crontab if needed
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
app = Celery("backend")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")

# Optionally, you can set up a periodic task directly in the celery.py file (instead of settings.py)
app.conf.beat_schedule = {
    'add-daily-profit-every-minute': {
        'task': 'backend.task.add_daily_profit',
        'schedule': 60.0,  # Every minute
    },
}