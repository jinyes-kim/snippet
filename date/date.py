from datetime import datetime
from pytz import timezone


def get_kst_datetime():
    return datetime.now(timezone('Asia/Seoul'))


def get_kst_timestamp():
    return datetime.now(timezone('Asia/Seoul')).timestamp()
