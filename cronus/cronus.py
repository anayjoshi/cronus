"""
Implements the cronus library
"""

import datetime
import time

loop_start_time = None
loop_duration = 0

def set_rate(rate):
    """Defines the ideal rate at which computation is to be performed

    Arguments:
    rate -- the frequency in Hertz (int or float)
    """
    if not (isinstance(rate, int) or isinstance(rate, float)):
        raise TypeError("argument to set_rate is expected to be int or float")
    global loop_duration
    loop_duration = 1.0/rate
    pass

def sleep():
    """Sleeps for a dynamic duration of time as determined by set_rate() and true()."""
    if loop_duration == 0:
        raise CronusError("call cronus.set_rate() before calling sleep")
    if loop_start_time == None:
        raise CronusError("call cronus.true() before calling sleep")
    td = datetime.datetime.now() - loop_start_time
    duration_to_sleep = loop_duration - td.total_seconds()
    if duration_to_sleep < 0:
        raise CronusError("skipping sleep. Too much work!")
    time.sleep(duration_to_sleep)

def true():
    """A substitute to True. Stores the time at which this function for use by sleep()"""
    global loop_start_time
    loop_start_time = datetime.datetime.now()
    return True


class CronusError:

    def __init__(self, msg):
        self.msg = msg
        pass

    def __str__(self):
        return self.msg
