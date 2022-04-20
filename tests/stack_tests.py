"""Unit tests for the stack data structure in the challenge module.

stack_tests contains test cases for the methods belonging to the stack class,
which provide a public interface for the stack data structure used to push a
key onto the stack, return the most recently added key, remove and return that
key, and determine whether the stack is empty.
"""

import unittest
from adts.stack import Stack

class StackTester(unittest.TestCase):
    """Contains the unit tests for the public interface of a stack."""

    #Setup runs before each test
    def setUp(self):
        self.stack = Stack()

    def test_push(self, new):
        """Tests the push method in the stack class.

        push introduces a new item at the top of the stack.

        Case: When multiple items are pushed onto the stack, the most recently
        added item should be at the top of the stack.
        """
        pass

    def test_top(self):
        """Tests the top method in the stack class.

        top returns the item at the top of the stack.

        Case: When multiple items are in the stack, the most recently added
        item should be returned by top.
        """
        pass

    def test_pop(self):
        """Tests the pop method in the stack class.

        pop removes and returns the item at the top of the stack.

        Case: When multiple items are on the stack, pop should remove and
        return the most recently added one.
        """
        pass

    def test_empty(self):
        """Tests the empty method in the stack class.

        empty returns true if there are no items on the stack, else false.

        Case: Empty called on a newly instantiated stack should return true,
        and then false once an item as been pushed onto it.
        """
        pass

if __name__ == '__main__':
    unittest.main()
