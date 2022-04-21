"""Implementation of a queue ADT using a doubly-linked list.

Queue is a first-in first-out data structure, meaning that the least-recently
added element is always the first to be removed. The interface for queue
includes methods which add a new element to the end of the queue, remove and
return the item at the front of the queue, and determine whether the queue is
empty.

My implementation of the queue data structure uses the linked-list that I have
already written, by adapting its interface the linked-list is easily made to
behave like a queue.
"""

from adts.list import List

class Queue:
    """Represents a queue data structure, providing a public interface for it.

    Functions in Queue are mapped to those of List, adapting the list data
    structure to the queue metaphor and FIFO priority.
    """
    def __init__(self):
        """Constructor for a queue.

        Arguments:
        self -- reference to the queue being constructed
        """
        self._queue = List()

    def enqueue(self, new):
        """Adds new to the back of the queue.

        Arguments:
        self -- reference to this queue instance
        new -- data to be enqueued
        """
        self._queue.push_back(new)

    def dequeue(self):
        """Removes and returns the item at the front of the queue.

        Arguments:
        self -- reference to this queue instance
        """
        return self._queue.pop_front()

    def empty(self):
        """Returns true if the queue is empty, else false.

        Arguments:
        self -- reference to this queue instance
        """
        return self._queue.empty()
