from datetime import datetime, timedelta
from pytz import timezone


def get_kst_datetime():
    return datetime.now(timezone("Asia/Seoul"))


def get_kst_timestamp():
    return datetime.now(timezone("Asia/Seoul")).timestamp()


def get_monday_of_this_week(current_time: datetime):
    monday = current_time - timedelta(day=current_time.weekday())

    return monday
