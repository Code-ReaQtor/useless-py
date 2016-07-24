#!/usr/bin/env python
import unittest
from useless.decorators import nocase

__author__ = 'Ronie Martinez'


class NoCaseTest(unittest.TestCase):

    def test_call_inexistent_snake_case(self):
        @nocase
        class MyClass(object):
            def myMethod(self):
                return "myMethod"

        a = MyClass()
        self.assertEquals("myMethod", a.myMethod())
        self.assertEquals("myMethod", a.my_method())

    def test_call_inexistent_camel_case(self):
        @nocase
        class MyClass(object):
            def my_method(self):
                return "my_method"

        a = MyClass()
        self.assertEquals("my_method", a.my_method())
        self.assertEquals("my_method", a.myMethod())


if __name__ == '__main__':
    unittest.main(verbosity=2)
