#!/usr/bin/env python
from useless.decorators import extends

__author__ = 'Ronie Martinez'


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
        return self.value * 3


# Warning! Read UPWARDS: Base1 is applied first before Base2... and so on...
@extends(Base2)
@extends(Base1)
class Derived2(object):
    pass

d2 = Derived2(10)
print d2.double()  # prints 20
print d2.triple()  # prints 30
