#!/usr/bin/env python
from useless import set_timeout

__author__ = 'Ronie Martinez'


def my_function():
    print "Hello world!"

set_timeout(my_function, 500)
