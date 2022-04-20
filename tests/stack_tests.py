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

    def test_push(self):
        """Tests the push method in the stack class.

        push introduces a new item at the top of the stack.

        Case: When multiple items are pushed onto the stack, the most recently
        added item should be at the top of the stack.
        """

        #Expected value at the top of the stack
        expected = "/home/ethan/Music"

        #Actual stack for which push is called
        self.stack.push("/home/ethan/Documents")
        self.stack.push("/home/ethan/Downloads")
        self.stack.push("/home/ethan/Music")
        actual = self.stack.top()

        #Assert expected and actual are the same string
        self.assertEqual(actual, expected)

    def test_top(self):
        """Tests the top method in the stack class.

        top returns the item at the top of the stack.

        Case: When multiple items are in the stack, the most recently added
        item should be returned by top.
        """

        #Expected value at the top of the stack
        expected = "/home/ethan/Templates"

        #Actual stack on which top is called
        self.stack.push("/home/ethan/Desktop")
        self.stack.push("/home/ethan/Public")
        self.stack.push("/home/ethan/Templates")

        #Assert expected and actual are the same string
        self.assertEqual(self.stack.top(), expected)

    def test_pop(self):
        """Tests the pop method in the stack class.

        pop removes and returns the item at the top of the stack.

        Case: When multiple items are on the stack, pop should remove and
        return the most recently added one.
        """

        #Expected value to be popped from the stack
        expected = "/home/ethan/Videos"

        #Actual stack with which to test pop
        self.stack.push("/home/ethan/Pictures")
        self.stack.push("/home/ethan/Games")
        self.stack.push("/home/ethan/Videos")
        actual = self.stack.pop()

        #Assert that the top item was returned by pop
        self.assertEqual(actual, expected)

    def test_empty(self):
        """Tests the empty method in the stack class.

        empty returns true if there are no items on the stack, else false.

        Case: Empty called on a newly instantiated stack should return true,
        and then false once an item as been pushed onto it.
        """

        #Stack should be empty before item is pushed
        self.assertTrue(self.stack.empty())

        #Push an item
        self.stack.push("/home")

        #Assert that the stack is no longer empty
        self.assertFalse(self.stack.empty())

if __name__ == '__main__':
    unittest.main()
