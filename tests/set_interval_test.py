#!/usr/bin/env python
import unittest
import time

from useless import set_interval, interval

__author__ = 'Ronie Martinez'


class SetIntervalTest(unittest.TestCase):
    def setUp(self):
        self.trigger_times = []

    def test_set_interval(self):
        def my_function(trigger_times):
            trigger_times.append(time.time())
        greenlet = set_interval(my_function, 500, self.trigger_times)
        time.sleep(3.1)  # make sure my_function is called 6 times
        greenlet.kill()
        self.assertTrue(all(round(t - s, 3) == 0.5 for s, t in zip(self.trigger_times, self.trigger_times[1:])))

    def test_interval_decorator(self):
        @interval(500)
        def my_function(trigger_times):
            trigger_times.append(time.time())
        greenlet = my_function(self.trigger_times)
        time.sleep(3.1)  # make sure my_function is called 6 times
        greenlet.kill()
        self.assertTrue(all(round(t - s, 3) == 0.5 for s, t in zip(self.trigger_times, self.trigger_times[1:])))

if __name__ == '__main__':
    unittest.main(verbosity=2)
