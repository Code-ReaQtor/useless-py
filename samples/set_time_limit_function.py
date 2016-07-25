#!/usr/bin/env python
from useless import set_time_limit, TimeLimitExceededError
import time

__author__ = 'Ronie Martinez'


def my_function():
    time.sleep(1)
    print "Hello world!"


# if time limit is enough
set_time_limit(my_function, 1500)
# if time limit is not enough, raises TimeLimitExceededError
try:
    set_time_limit(my_function, 500)
except TimeLimitExceededError as e:
    print e.message
