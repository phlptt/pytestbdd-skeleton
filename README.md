# pytestbdd-skeleton

This is a basic skeleton repo to run pytest-bdd tests on chrome browser.

## Prerequisites
    * Python 3
    * pip
```shell
    curl https://bootstrap.pypa.io/get-pip.py | python
```
    * pipenv
```shell
    pip install --user pipenv
``` 
    * Chrome browser - https://www.google.com/intl/en_uk/chrome/
    * Mac only

## Setup
    * To install dependencies 
```shell
pipenv sync -d
```
    * To run tests: 
```shell
pipenv run python -m pytest
```
    * To run specific test tag: 
```shell
pipenv run python -m pytest -m 'tag_here'
```
