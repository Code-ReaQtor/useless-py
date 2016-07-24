#!/usr/bin/env python
from useless import time_limit, TimeLimitExceededError
import time

__author__ = 'Ronie Martinez'


@time_limit(1500)
def my_function1():
    time.sleep(1)
    print "Hello world!"


@time_limit(500)
def my_function2():
    time.sleep(1)
    print "Hello world!"


# if time limit is enough
my_function1()
# if time limit is not enough, raises TimeLimitExceededError
try:
    my_function2()
except TimeLimitExceededError as e:
    print e.message
