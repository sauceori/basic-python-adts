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
        self.assertEqual(actual, expected)

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
        self.assertTrue(self.queue.empty())

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

    def test_phonebook(self):
        """Acceptance test for the Queue class.

        An automatic telemarketer gives a prerecorded phonecall to each new
        number added to its "phonebook." The message is generic, so the only
        information the system needs is the number to be called. The system
        calls numbers in the queue until none are left on a first-come
        first-serve basis, removing them as it goes.
        """

        #Add numbers to the system's "phonebook"
        numbers = ["540-270-3992", "618-625-6145", "601-645-8633", "941-796-3151"]
        for number in numbers:
            self.queue.enqueue(number)

        #The system forgets the numbers as it calls each one sequentially
        while self.queue.empty() == False:
            call_no = self.queue.dequeue()
            print("Call Sent to " + call_no)

        #New numbers are fed to the system
        numbers = ["360-789-7698", "704-524-6530", "432-978-7038", "817-762-5518"]
        for number in numbers:
            self.queue.enqueue(number)

        #Call all the new numbers
        while self.queue.empty() == False:
            call_no = self.queue.dequeue()
            print("Call Sent to " + call_no)

        #All numbers should be run through at this point
        self.assertTrue(self.queue.empty())

if __name__ == '__main__':
    unittest.main()
