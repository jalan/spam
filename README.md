# spam

[![Build Status](https://travis-ci.org/jalan/spam.svg?branch=master)](https://travis-ci.org/jalan/spam)
[![Coverage Status](https://coveralls.io/repos/github/jalan/spam/badge.svg?branch=master)](https://coveralls.io/github/jalan/spam?branch=master)

An example Python C extension module, based on
[the fantastic official documentation](https://docs.python.org/3/extending/).
The module itself doesn't do anything useful, but serves as a demonstration of

 - Python 2 and 3 support
 - some functions
 - an exception type
 - tests
 - continuous integration via [Travis](https://travis-ci.org)
 - code coverage via [Coveralls](https://coveralls.io)

Consider it a starting point for building a new extension.


## Build

You need a C compiler and the Python development libraries.

On Debian, Ubuntu, and friends:

```
sudo apt-get update
sudo apt-get install build-essential python-dev
```

On Fedora, Red Hat, and friends:

```
sudo yum install gcc python-devel redhat-rpm-config
```

Then

```
python setup.py build
```


## Tests

```
python setup.py test
```
