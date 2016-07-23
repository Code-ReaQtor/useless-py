#!/usr/bin/env python
import unittest
import time

from useless import set_time_limit, TimeLimitExceededError, time_limit

__author__ = 'Ronie Martinez'


class SetTimeLimitTest(unittest.TestCase):

    def test_set_time_limit(self):
        def my_function():
            return 100
        x = set_time_limit(my_function, 500)
        self.assertEquals(x, 100)

    def test_set_time_limit_of_long_function(self):
        def my_function():
            time.sleep(1)
            return 100
        with self.assertRaises(TimeLimitExceededError):
            set_time_limit(my_function, 500)

    def test_time_limit_decorator(self):
        @time_limit(500)
        def my_function():
            return 100
        x = my_function()
        self.assertEquals(x, 100)

    def test_time_limit_decorator_of_long_function(self):
        @time_limit(500)
        def my_function():
            time.sleep(1)
            return 100
        with self.assertRaises(TimeLimitExceededError):
            my_function()


if __name__ == '__main__':
    unittest.main(verbosity=2)
