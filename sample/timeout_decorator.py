#!/usr/bin/env python
from useless import timeout

__author__ = 'Ronie Martinez'


@timeout(1000)
def my_function():
    print "Hello world!"

my_function()
