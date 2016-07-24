#!/usr/bin/env python
from useless.decorators import nocase

__author__ = 'Ronie Martinez'


@nocase
class MyClass(object):

    def my_method(self):
        return "my_method"

    def myOtherMethod(self):
        return "myOtherMethod"


a = MyClass()
print a.my_method()  # prints my_method
print a.myMethod()  # prints my_method
print a.myOtherMethod()  # prints myOtherMethod
print a.my_other_method()  # prints myOtherMethod
