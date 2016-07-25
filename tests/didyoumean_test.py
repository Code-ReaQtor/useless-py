#!/usr/bin/env python
from __future__ import print_function
import unittest

from useless.decorators import didyoumean
from useless.exceptions import DidYouMeanError

__author__ = 'Ronie Martinez'


class DidYouMean(unittest.TestCase):

    def test_raises(self):
        @didyoumean
        class MyClass(object):
            def ello(self):
                pass

            def hello_world(self):
                pass

        a = MyClass()
        with self.assertRaises(DidYouMeanError):
            a.hello()

    def test_message(self):
        @didyoumean
        class MyClass(object):
            def ello(self):
                pass

            def hello_world(self):
                pass

        a = MyClass()
        try:
            a.hello()
        except DidYouMeanError as e:
            self.assertIn("Did you mean one of these?", e.message)
            self.assertItemsEqual(e.close_matches, ["hello_world", "ello"])

    def test_DidYouMeanError_is_AttributeError(self):
        @didyoumean
        class MyClass(object):
            def ello(self):
                pass

            def hello_world(self):
                pass

        a = MyClass()
        try:
            a.hello()
        except AttributeError as e:
            self.assertIn("Did you mean one of these?", e.message)
        self.assertTrue(issubclass(DidYouMeanError, AttributeError))


if __name__ == '__main__':
    unittest.main(verbosity=2)
