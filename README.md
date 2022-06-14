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
    * run 
```shell
pipenv sync -d
```
    * to run tests run 
```shell
pipenv run python -m pytest
```
    * to run specific tag run 
```shell
pipenv run python -m pytest -m 'tag_here'
```
