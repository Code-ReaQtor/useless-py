# Change Log
List of changes to useless-py

## [Unreleased]

## [1.0.3.a] - 2016-07-26
### Fixed
- Added exceptions.py to MANIFEST

## [1.0.3] - 2016-07-25
### Added
- @nocase decorator - class decorator allowing access to attributes regardless of coding style (camelCase or snake_case)
- @didyoumean decorator - class decorator, raises DidYouMeanError (subclass of AttributeError) which suggest close matches

## [1.0.2] - 2016-07-24
### Added
- @extends decorator - inheritance using a class decorator

## [1.0.1] - 2016-07-23
### Added
- set_interval function (similar to Javascript's setInterval using gevent)
- @interval decorator (decorator for set_interval)
- set_timeout function (similar to Javascript's setTimeout using gevent)
- @timeout decorator (decorator for set_timeout)
- set_time_limit function - limits the maximum execution time of a function
- @time_limit decorator (decorator for set_time_limit)

[Unreleased]: https://github.com/Code-ReaQtor/useless-py/compare/v1.0.3.a...master
[1.0.3.a]: https://github.com/Code-ReaQtor/useless-py/releases/tag/1.0.3.a
[1.0.3]: https://github.com/Code-ReaQtor/useless-py/releases/tag/1.0.3
[1.0.2]: https://github.com/Code-ReaQtor/useless-py/releases/tag/1.0.2
[1.0.1]: https://github.com/Code-ReaQtor/useless-py/releases/tag/1.0.1