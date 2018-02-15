# travis-test-bob

[![Build Status](https://travis-ci.org/acostapazo/travis-test-bob.svg?branch=master)](https://travis-ci.org/acostapazo/travis-test-bob)
[![Doc](http://img.shields.io/badge/docs-latest-orange.svg)](https://acostapazo.github.io/travis-test-bob/)

This package is created only for learning proposes. 

Following the instruction below, we have added ci into this project using travis:


- [Travis CI: Getting started](https://docs.travis-ci.com/user/getting-started/)
- [Using conda with Travis CI](https://conda.io/docs/user-guide/tasks/use-conda-with-travis-ci.html)


##### Environment

~~~
 $ conda env create -f environment.yml
 $ source activate travis-test-bob
~~~

##### Install

~~~
 $ python boostrap-buildout.py
 $ bin/buildout
~~~

##### Tests

~~~
 $ bin/nosetests -v
~~~

##### Script

~~~
 $ bin/script_example.py
~~~


##### Documentation

~~~
 $ bin/sphinx-build -b html doc/ doc/html
~~~
