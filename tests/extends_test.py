#!/usr/bin/env python
import unittest
from useless.decorators import extends

__author__ = 'Ronie Martinez'


class ExtendsTest(unittest.TestCase):
    def test_single_extends(self):
        class Base(object):
            def __init__(self, value):
                self.value = value

            def double(self):
                return self.value * 2

            def triple(self):
                return self.value * 3

        @extends(Base)
        class Derived(object):
            def double(self):
                return self.value * 3

        d = Derived(10)
        self.assertIsInstance(d, Base)
        self.assertIsInstance(d, Derived)
        self.assertEquals(30, d.double())
        self.assertEquals(30, d.triple())

    def test_multiple_extends(self):
        class Base1(object):
            def __init__(self, value):
                self.value = value

            def double(self):
                return self.value * 2

        class Base2(object):
            def __init__(self, value):
                self.value = value

            def double(self):
                return self.value * 4

            def triple(self):
                return self.value * 10

        # Warning! Read UPWARDS: Base1 is applied first before Base2... and so on...
        @extends(Base2)
        @extends(Base1)
        class Derived(object):
            pass

        d = Derived(10)
        self.assertIsInstance(d, Base1)
        self.assertIsInstance(d, Base2)
        self.assertIsInstance(d, Derived)
        self.assertEquals(20, d.double())
        self.assertEquals(100, d.triple())

if __name__ == '__main__':
    unittest.main(verbosity=2)
