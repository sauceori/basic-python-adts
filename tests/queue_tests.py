"""Unit tests for the queue data structure in the challenge module.

queue_tests contains test cases for the methods belonging to the queue class,
which provide a public interface for the queue data structure used to add a new
node to the back of the queue, remove and return the item at the front of the
queue, and determine whether the queue is empty.
"""

import unittest
from adts.queue import Queue

class QueueTester(unittest.TestCase):
    """Contains the unit tests for the public interface of a queue."""

    #Setup runs before each test
    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        """Tests the enqueue method in the Queue class.

        Adds a new element to the back of the queue.

        Case: When multiple items are queued, the most recently queued item
        should be added at the end of the queue.
        """

        #Expected value at the front of the queue
        expected = "941-796-3151"

        #Actual, enqueue some elements
        self.queue.enqueue("941-796-3151")
        self.queue.enqueue("601-645-8633")
        self.queue.enqueue("618-625-6145")
        actual = self.queue.dequeue()

        #Assert that the returned value is as expected
        assertEqual(actual, expected)

    def test_dequeue(self):
        """Tests the dequeue method in the Queue class.

        Removes and returns the item at the front of the queue.

        Case: With a queue containing multiple items, dequeue can be used to
        "serve" all elements in an array thereby removing them.
        """

        #Enqueue some elements
        self.queue.enqueue("941-796-3151")
        self.queue.enqueue("601-645-8633")
        self.queue.enqueue("618-625-6145")

        #Dequeue those elements
        self.queue.dequeue()
        self.queue.dequeue()
        self.queue.dequeue()

        #After three enqueues and three dequeues, queue should be empty
        assertFalse(self.queue.empty())

    def test_empty(self):
        """Tests the empty method in the Queue class.

        Returns true if the queue is empty, else false.

        Case: The empty method should return true until an item is enqueued.
        """

        #Queue should be empty before item is pushed
        self.assertTrue(self.queue.empty())

        #Push an item
        self.queue.enqueue("540-270-3992")

        #Assert that the queue is no longer empty
        self.assertFalse(self.queue.empty())

if __name__ == '__main__':
    unittest.main()
