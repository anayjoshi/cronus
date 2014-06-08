"""
Test cases for beat module

Author: Anay
Date created: 20th May 2014
"""

import beat
import time
import datetime
from nose.tools import assert_raises, assert_equals, assert_true

class TestCronus:

    def setup(self):
        pass

    def teardown(self):
        beat.loop_start_time = None
        beat.loop_duration = 0

    def test_type_checking_in_set_rate(self):
        """Tests that set_rate() throws TypeError if argument is string"""
        assert_raises(TypeError, lambda: beat.set_rate("hi"))

    def test_exception_when_no_rate(self):
        """Tests that BeatError is raised when sleep() is called before
        calling set_rate()"""
        beat.true()
        assert_raises(beat.BeatError, beat.sleep)

    def test_exception_when_no_true(self):
        """Tests that BeatError is raised when sleep() is called before
        calling true()"""
        beat.set_rate(2)
        assert_raises(beat.BeatError, beat.sleep)

    def test_normal_operation(self):
        """Tests that beat sleeps for approproate duration in normal operation"""
        beat.set_rate(2)
        assert_true(beat.true())
        time.sleep(0.2)
        time_before = datetime.datetime.now()
        beat.sleep()
        time_after = datetime.datetime.now()
        time_slept_by_beat = time_after - time_before
        assert (abs(time_slept_by_beat.microseconds - 300000) < 10000)
