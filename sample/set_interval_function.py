#!/usr/bin/env python
from useless import set_interval
import time

__author__ = 'Ronie Martinez'


def my_function():
    print "Hello world!"

set_interval(my_function, 500)  # Caution! Non-blocking.
time.sleep(10)  # Write some blocking code
