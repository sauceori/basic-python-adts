#!/bin/sh

#Simple script to execute all my test cases

python -m unittest tests/list_tests.py
python -m unittest tests/stack_tests.py
python -m unittest tests/queue_tests.py
