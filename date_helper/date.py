from datetime import datetime, timedelta
from pytz import timezone


# TODO: 항상 UTC를 기준으로 변경하도록 변경
def get_kst_datetime():
    return datetime.now(timezone("Asia/Seoul"))


def get_kst_timestamp():
    return datetime.now(timezone("Asia/Seoul")).timestamp()


def get_monday_of_this_week(current_time: datetime):
    monday = current_time - timedelta(day=current_time.weekday())

    return monday
