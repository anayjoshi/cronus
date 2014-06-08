"""
Implements the timeout decorator, and the TimeoutError exception.

The timeout mechanism is implemented using UNIX signals. As of now,
only integer value for timeouts in permitted

Author: Anay
Date created: 8th June 2014
"""

import signal

class TimeoutError(Exception):

    """Thrown by @timeout decorator when the external function exceeds\
            the timeout duration"""

    def __init__(self):
        pass

    def __str__(self):
        pass

def timeout(duration):
    """
    A decorator to force a time limit on the execution of an external function.

    :param int duration: the timeout duration

    :raises: TypeError, if duration is anything other than integer

    :raises: ValueError, if duration is a negative integer

    :raises TimeoutError, if the external function execution crosses 'duration' time

    """
    if not isinstance(duration, int):
        raise TypeError("timeout duration should be a positive integer")
    if duration <= 0:
        raise ValueError("timeoutDuration should be a positive integer")

    def decorator(func):
        def wrapped_func(*args, **kwargs):
            try:
                def alarm_handler(signum, stack):
                    raise TimeoutError()
                signal.signal(signal.SIGALRM, alarm_handler)
                signal.alarm(duration)
                reply = func(*args, **kwargs)
            except TimeoutError as e:
                raise e
            return reply
        return wrapped_func
    return decorator
