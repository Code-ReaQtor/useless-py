#!/usr/bin/env python
from useless.decorators import extends

__author__ = 'Ronie Martinez'


class Base1(object):
    def __init__(self, value):
        self.value = value

    def double(self):
        return self.value * 2


@extends(Base1)
class Derived1(object):
    pass

d1 = Derived1(10)
print d1.double()  # prints 20
