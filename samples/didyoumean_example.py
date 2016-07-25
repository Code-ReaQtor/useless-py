#!/usr/bin/env python
from useless.decorators import didyoumean

__author__ = 'Ronie Martinez'

@didyoumean
class MyClass(object):
    def ello(self):
        pass

    def hello_world(self):
        pass


a = MyClass()
try:
    a.hello()
except AttributeError as e:  # DidYouMeanError is a subclass of AttributeError, no need to import
    print(e.message)
