from celery import shared_task
from django.utils.timezone import now
import datetime
from .models import Deposit


@shared_task
def add_daily_profit():
    today = now().date()
    weekday = today.weekday()  # Monday=0, Tuesday=1, ..., Sunday=6

    # Only run on Monday, Tuesday, Wednesday, Thursday, and Monday
    valid_profit_days = {0, 1, 2, 3, 4}  # Monday to Thursday

    if weekday in valid_profit_days:
        deposits = Deposit.objects.filter(status="APPROVED")

        for deposit in deposits:
            if deposit.profit_start_date:
                deposit.user.profit += deposit.amount * 0.01  # 1% profit
                deposit.user.save()
