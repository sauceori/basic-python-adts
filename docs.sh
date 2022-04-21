#!/bin/sh

#Simple script to generate all my docs and move them to the appropriate folder

pydoc -w adts/list.py
pydoc -w adts/stack.py
pydoc -w adts/queue.py

pydoc -w tests/list_tests.py
pydoc -w tests/stack_tests.py
pydoc -w tests/queue_tests.py

mv *.html docs
