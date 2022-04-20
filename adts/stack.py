"""Implementation of a stack ADT using a doubly-linked list.

Stack is a last-in first-out data structure, meaning the most recently added
element is allways the first to be removed. The interface for stack includes
functions to add an item to the top of the stack, return the most recently
added key, remove and return the most recently added key, and determine whether
the stack is empty.

My implementation of the stack data structure uses the linked-list that I have
already written, by changing its interface the linked-list is easily made to
behave like a stack.
"""

from adts.list import List

class Stack:
    """Represents the stack data type, providing a public interface for it.

    By mapping Stack functions to those belonging to List, the linked-list
    metaphor is effectively changed to that of a stack.
    """
    def __init__(self):
        """Constructor for a stack.

        Arguments:
        self -- reference to the node being constructed
        """
        self.stack = List()

    def push(self, new):
        """Adds new to the top of the stack.

        Arguments:
        self -- reference to the node being constructed
        """
        self.stack.push_back(new)

    def top(self):
        """Returns the item at the top of the stack

        Arguments:
        self -- reference to the node being constructed
        """
        return self.stack.top_back()

    def pop(self):
        """Removes the item at the top of the stack, returns it.

        Arguments:
        self -- reference to the node being constructed
        """
        return self.stack.pop_back()

    def empty(self):
        """Returns true if the stack is empty, else false.

        Arguments:
        self -- reference to the node being constructed
        """
        return self.stack.empty()
