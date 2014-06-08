"""
Tests for @timeout decorator

Author: Anay
Date created: 8th June 2014
"""
from timeout import timeout, TimeoutError
import time
from nose.tools import assert_raises, assert_equals

class TestTimeout:
    
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_timeout_with_timeout_error(self):
        """Tests that TimeoutError is thrown for long functions"""
        @timeout(1)
        def dummy_computation():
            time.sleep(2)
        
        with assert_raises(TimeoutError) as cm:
            dummy_computation()

    def test_timeout_without_timeout_error(self):
        """Tests that for small functions, TimeoutError is not thrown"""
        @timeout(1)
        def dummy_computation():
            time.sleep(0.2)
            return 5

        assert_equals(dummy_computation(), 5)

    def test_value_and_type_errors(self):
        """Tests that ValueError & TypeError are thrown for incorrect furation"""

        with assert_raises(TypeError) as cm:
            @timeout(0.2)
            def dummy_computation():
                pass
        with assert_raises(ValueError) as cm:
            @timeout(-3)
            def dummy_computation():
                pass
