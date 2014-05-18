import datetime
import time

loop_start_time = None
loop_duration = 0

def set_rate(rate):
    global loop_duration
    loop_duration = 1.0/rate
    pass

def sleep():
    global loop_start_time
    td = datetime.datetime.now() - loop_start_time
    duration_to_sleep = loop_duration - td.total_seconds()
    time.sleep(duration_to_sleep)
    pass


def true():
    global loop_start_time
    loop_start_time = datetime.datetime.now()
    return True

