#!/usr/bin/env python
import unittest
import time

from useless import set_timeout, timeout

__author__ = 'Ronie Martinez'


class SetTimeoutTest(unittest.TestCase):

    def test_set_timeout(self):
        def my_function():
            return 100
        start = time.time()
        result = set_timeout(my_function, 500)
        end = time.time()
        self.assertEquals(100, result)
        self.assertGreaterEqual(end-start, 0.5)

    def test_timeout_decorator(self):
        @timeout(500)
        def my_function():
            return 100
        start = time.time()
        result = my_function()
        end = time.time()
        self.assertEquals(100, result)
        self.assertGreaterEqual(end-start, 0.5)


if __name__ == '__main__':
    unittest.main(verbosity=2)
