"""
Test cases for cronus module
"""

import cronus
import time
import datetime
from nose.tools import assert_raises

class TestCronus:

    def setup(self):
        pass

    def teardown(self):
        cronus.loop_start_time = None
        cronus.loop_duration = 0
        pass

    def test_type_checking_in_set_rate(self):
        """Tests that set_rate() throws TypeError if argument is string"""
        assert_raises(TypeError, lambda: cronus.set_rate("hi"))

    def test_exception_when_no_rate(self):
        """Tests that CronusError is raised when sleep() is called before
        calling set_rate()"""
        cronus.true()
        assert_raises(cronus.CronusError, cronus.sleep)
        pass

    def test_exception_when_no_true(self):
        """Tests that CronusError is raised when sleep() is called before
        calling true()"""
        cronus.set_rate(2)
        assert_raises(cronus.CronusError, cronus.sleep)
        pass

#TODO: use mocking instead of actually calling time.sleep() function
    def test_normal_operation(self):
        """Tests that cronus sleeps for approproate duration in normal operation"""
        cronus.set_rate(2)
        assert(cronus.true())
        time.sleep(0.2)
        time_before = datetime.datetime.now()
        cronus.sleep()
        time_after = datetime.datetime.now()
        time_slept_by_cronus = time_after - time_before
        assert abs(time_slept_by_cronus.microseconds - 300000) < 10000
