![version](https://img.shields.io/pypi/v/useless-py.svg)![license](https://img.shields.io/pypi/l/useless-py.svg)![status](https://img.shields.io/pypi/status/useless-py.svg)

# useless-py
Useful python utilities with less effort.

## Installation:
```sh
pip install useless-py
```

## Features:
- set_interval() function and @interval decorator - similar to Javascript's setInterval() method, uses gevent
- set_timeout() function and @timeout decorator - similar to Javascript's setTimeout() method, uses gevent
- set_time_limit() function and @time_limit decorator - limits the maximum execution time of a function, raises TimeLimitExceededError
- @extends decorator - inheritance using a class decorator, inspired by Java's extends
- @nocase decorator - class decorator that allows access to attributes regardless of coding style (camelCase or snake_case)

## Usage:
Check "sample" folder.

## To-Do:
- [ ] Class Decorators
    - [x] @extends - like Java's (instead of direct inheritance). IMO, more readable when you are doing multiple inheritance.
    - [ ] @implements - like Java's (with the help of python "abc" module).
    - [x] @nocase - rewrite of "nocase" module using a class decorator instead of direct inheritance, more Pythonic, IMO. (https://pypi.python.org/pypi/nocase)
    - [ ] @DidYouMean - raises a "DidYouMean" exception (instead of AttributeError) when an attribute of an instance does not exist and suggests close matches. Think of "git" when you messed up on giving the correct argument:
    ```sh
    C:\Users\Ronie Martinez>git hello
    git: 'hello' is not a git command. See 'git --help'.
    Did you mean one of these?
            help
            reflog
    ```
- [ ] Context Managers
    - [ ] Regular expressions in a "with" statement - I miss the old Perl $1, $2, $3 (special variables)... but global variable is an overkill, let's make a more Pythonic feature 
 
## Author:
* Ronie Martinez (ronmarti18@gmail.com)
