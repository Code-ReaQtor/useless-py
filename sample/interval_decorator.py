#!/usr/bin/env python
from useless import interval
import time

__author__ = 'Ronie Martinez'


@interval(500)
def my_function():
    print "Hello world!"

my_function()  # Caution! Non-blocking.
time.sleep(10)  # Write some blocking code
