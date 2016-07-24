![version](https://img.shields.io/pypi/v/useless-py.svg)![license](https://img.shields.io/pypi/l/useless-py.svg)![status](https://img.shields.io/pypi/status/useless-py.svg)

# useless-py
Useful python utilities with less effort.

## Installation:
```sh
pip install useless-py
```

## Usage:

### set_interval() function
```python
from useless import set_interval
import time


def my_function():
    print "Hello world!"

set_interval(my_function, 500)  # Caution! Non-blocking.
time.sleep(10)  # Write some blocking code

```

### @interval decorator
```python
from useless import interval
import time


@interval(500)
def my_function():
    print "Hello world!"

my_function()  # Caution! Non-blocking.
time.sleep(10)  # Write some blocking code

```

### set_timeout() function
```python
from useless import set_timeout


def my_function():
    print "Hello world!"

set_timeout(my_function, 500)

```

### @timeout decorator
```python
from useless import timeout


@timeout(1000)
def my_function():
    print "Hello world!"

my_function()

```

### set_time_limit() function
```python
from useless import set_time_limit, TimeLimitExceededError
import time


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

```

### @time_limit decorator
```python
from useless import time_limit, TimeLimitExceededError
import time


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

```

## To-Do:
- [ ] Class Decorators
    - [ ] @extends - like Java's (instead of direct inheritance). IMO, more readable when you are doing multiple inheritance.
    - [ ] @implements - like Java's (with the help of python "abc" module, we are just adding).
    - [ ] @nocase - rewrite of "nocase" module using a class decorator instead of direct inheritance, more Pythonic, IMO. (https://pypi.python.org/pypi/nocase)
    - [ ] @DidYouMean - raises a "DidYouMean" exception (instead of AttributeError) when an attribute of an instance does not exist and suggests close matches. Think of "git" when you messed up on giving the correct argument:
    ```sh
    C:\Users\Ronie Martinez>git hello
    git: 'hello' is not a git command. See 'git --help'.
    Did you mean one of these?
            help
            reflog
    ```
- [ ] Context managers
    - [ ] Regular expressions in a "with" statement - I miss the old Perl $1, $2, $3 (special variables)... but global variable is an overkill, let's make a more Pythonic feature 
 
## Author:
* Ronie Martinez (ronmarti18@gmail.com)
