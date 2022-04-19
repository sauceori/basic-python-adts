"""Unit tests for the linked-list data structure in the challenge module.

list_tests contains test cases for the methods belonging to the list class,
which provide a public interface for the linked list data structure used to
add or remove nodes, find and erase nodes, and determine whether the list is
empty among other uses.
"""

import unittest
from adts.list import List

class ListTester(unittest.TestCase):
    """Contains the unit tests for the public interface of a linked list.
    """

    #Setup runs before each test
    def setUp(self):
        self.list = List()

    def test_push_front(self):
        """Tests the push_front method in the list class.

        push_front should introduce a new node at the beginning of the list
        such that the next element in the list points backwards to it.

        Case: A number of values are pushed to the front of the list, is the
        last one added at the head of the list?
        """

        #Expected value at the head of the list
        expected = 5

        #Actual list for which push_front is called
        for x in range(6):
            self.list.push_front(x)
        actual = self.list.head.next.prev.data

        #Assert expected and the head of actual are equal
        self.assertEquals(actual, expected)

    def test_top_front(self):
        """Tests the top_front method in the list class.

        top_front should return the front item, the head of the list.

        Case: The head of the list is the only element in a linked list which
        lacks a prev pointer, so in a linked list with many elements top_front
        should return a node whose prev value is "None."
        """

        #Expected data at the head of the list
        expected_data = 'z'
        expected_prev = None

        #Actual list on which top_front is called
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for letter in alphabet:
            self.list.push_front(letter)
        actual = top_front(self.list)

        #Assert that the node at the head is as expected
        self.assertEquals(actual.data, expected_data)
        self.assertEquals(actual.prev, expected_prev)

    def test_pop_front(self):
        """Tests the pop_front method in the list class.

        pop_front should return the front item, removing it from the list.

        Case: In a list with multiple elements, pop_front should removes the
        current head such that the next sequential node is the new head.
        """

        #Expected data returned from pop_front
        expected_old = 'saturday'

        #Expected data at the new head
        expected_new = 'friday'

        #Actual list on which pop_front is called
        week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        for day in week:
            self.list.push_front(day)
        actual_old = self.list.pop_front().data
        actual_new = self.list.head.data

        #Assert the data at the new and old head is as expected
        self.assertEquals(actual_old, expected_old)
        self.assertEquals(actual_new, expected_new)

    def test_push_back(self):
        """Tests the push_back method in the list class.

        push_back should introduce a new tail to the list such that the old
        tail points to it.

        Case: A number of values are pushed to the back of the list, the tail
        of the list should be the last value pushed.
        """

        #Expected value at the end of the list
        expected = "dec"

        #Actual list on which push_back is called
        year = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
        for month in year:
            self.list.push_back(month)
        actual = self.list.tail.prev.next.data

        #Assert the tail is as expected
        self.assertEquals(actual, expected)

    def test_top_back(self):
        """Tests the top_back method in the list class.

        top_back should return the tail node of the list.

        Case: In a list with many nodes, the tail is the only one with a next
        pointer equal to "None" because it represents the end of the list.
        """

        #Expected data at the end of the list
        expected_data = 5
        expected_next = None

        #Actual list on which top_back is called
        for x in range(6):
            self.list.push_back(x)
        actual = list.top_back()

        #Assert the node at the tail is as expected
        self.assertEquals(actual.data, expected_data)
        self.assertEquals(actual.next, expected_next)

    def test_pop_back(self):
        """Tests the pop_back method in the list class.

        pop_back should return the item at the back of the list, removing it.

        Case: In a list with multiple nodes, pop_back removes the tail such
        that the node before it is the new tail node.
        """

        #Expected data returned by pop_back
        expected_old = 'z'

        #Expected data in the new tail
        expected_new = 'y'

        #Actual list on which pop_back is called
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for letter in alphabet:
            self.list.push_back(letter)
        actual_old = self.list.pop_back().data
        actual_new = self.list.tail.data

        #Assert the data at the new and old tail are as expected
        self.assertEquals(actual_old, expected_old)
        self.assertEquals(actual_new, expected_new)

    def test_find(self):
        """Tests the find method in the list class.

        find should return true if the data passed to it exists in the list.

        Case: An item is added to a list of elements, attempting to find this
        element should return false before and true after it is added.
        """

        #Here, expected is the value the value the find function searches for
        expected = 'wednesday'

        #Actual list the find function is working on
        self.list.push_back('sunday')
        self.list.push_back('monday')
        self.list.push_back('tuesday')

        #Expected is not in the list yet
        self.assertFalse(self.list.find(expected))

        #Add expected to the list
        self.list.push_back('wednesday')

        #Assert that expected can now be found in the list
        self.assertTrue(self.list.find(expected))

    def test_erase(self):
        """Tests the erase method in the list class.

        erase removes the first instance of the specified value in the list.

        Case: In a list with multiple elements that have the same value, erase
        should remove the node containing that value without touching the others.
        """

        #Expected data for the head and tail after a third element is removed
        expected_head = 'feb'
        expected_tail = 'jan'

        #Actual list the erase function is working on
        self.list.push_back('jan')
        self.list.push_back('feb')
        self.list.push_back('jan')

        #Call the erase function on the list
        self.list.erase('jan')
        actual_head = self.list.head.data
        actual_tail = self.list.tail.data

        #Assert that the head is 'feb' after having removed the old 'jan'
        self.assertEquals(actual_head, expected_head)

        #Assert that the second instance of 'jan' hasn't been removed
        self.assertEquals(actual_tail, expected_tail)

    def test_empty(self):
        """Tests the empty method in the list class.

        empty returns true if the list contains no nodes.

        Case: If a list is empty, then empty should return true. Once a node is
        added to the list, it should return false.
        """

        #The list should be empty at this point in the test
        self.assertTrue(self.list.empty())

        #Add an element to the list
        self.list.push_back(1)

        #The list now has an element, empty should return false
        self.assertFalse(self.list.empty())

    def test_add_before(self):
        """Tests the add_before method in the list class.

        add_before inserts a node containing the specified data before a
        specified node.

        Case: In a list with other nodes, add_before places the specified data
        before the specified node, if that node happens to be at the beginning
        of the list then the addition becomes the new head.
        """

        #Expected head and tail after insertion
        expected_head = 0
        expected_tail = 1

        #Actual list
        self.list.push_back(1)
        self.list.add_before(1, 0)

        #Actual head and tail values
        actual_head = self.list.head.data
        actual_tail = self.list.tail.data

        #Assert that the head and tail values are as expected
        self.assertEquals(actual_head, expected_head)
        self.assertEquals(actual_tail, expected_tail)

    def test_add_after(self):
        """Tests the add_after method in the list class.

        add_after inserts a node containing the specified data before a
        specified node.

        Case: In a list with other nodes, add_after places the specified data
        after the specified node, if that node happens to be at the beginning
        of the list then the addition becomes the new head.
        """

        #Expected head and tail after insertion
        expected_head = 0
        expected_tail = 1

        #Actual list
        self.list.push_back(0)
        self.list.add_after(0, 1)

        #Actual head and tail values
        actual_head = self.list.head.data
        actual_tail = self.list.tail.data

        #Assert that the head and tail values are as expected
        self.assertEquals(actual_head, expected_head)
        self.assertEquals(actual_tail, expected_tail)

if __name__ == '__main__':
    unittest.main()
