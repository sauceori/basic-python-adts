"""Implementation of a doubly linked list ADT.

Each node in a doubly-linked list contains references to both the previous and
next elements in the list. The "head" and "tail" nodes do not point to
previous and next nodes, respectively. The interface for this list includes
functions used to insert or return elements at the head or tail, remove those
elements, find whether a value exists in the list, erase a values from the
list, determine whether the list is empty, and add nodes before or after other
specified nodes.
"""

class Node:
    """Represents a single node, the basic unit used to build linked lists.

    Node contains a data value (which may also be referred to as a key) as well
    as references to the next and previous nodes in the list. Having nodes with
    references to both the previous and next elements in the list distinguishes
    this node from one in a singly-linked list.
    """
    def __init__(self, data=None):
        """Constructor for a doubly-linked list node.

        Arguments:
        self -- reference to the node being constructed
        data -- the value to be put in the node (default None)
        """
        self.data = data
        self.prev = None
        self.next = None

class List:
    """Represents a doubly-linked list, and provides a public interface for it.

    List maintains references to the head and tail nodes in the list, which can
    be accessed or mutated in and of themselves or used as "access points"
    by it's methods, through which the list can be traversed so that the
    interior nodes can be accessed or modified.
    """
    def __init__(self):
        """Constructor for a linked list.

        Arguments:
        self -- reference to the node being constructed
        """

        self.head = None
        self.tail = None

    def push_front(self, new):
        """Adds a new node at the front of the list, replacing the head node.

        Arguments:
        self -- reference to this list instance
        new -- data value for the new node
        """
        pass

    def top_front(self):
        """Returns the value at the front of the list.

        Arguments:
        self -- reference to this list instance
        """
        pass

    def pop_front(self):
        """Removes the front item and returns its data.

        Arguments:
        self -- reference to this list instance
        """
        pass

    def push_back(self, new):
        """Adds a new node at the back of the list, replacing the tail node.

        Arguments:
        self -- reference to this list instance
        new -- data value for the new node
        """
        pass

    def top_back(self):
        """Returns the value at the end of the list.

        Arguments:
        self -- reference to this list instance
        """
        pass

    def pop_back(self):
        """Removes the front item and returns its data.

        Arguments:
        self -- reference to this list instance
        """
        pass

    def find(self, key):
        """Returns true if the key is in the list, else false.

        Arguments:
        self -- reference to this list instance
        key -- the value to be searched for in the list
        """
        pass

    def erase(self, key):
        """Removes the first instance of the key fron the list, if it exists.

        Arguments:
        self -- reference to this list instance
        key -- the value to be removed from the list
        """
        pass

    def empty(self):
        """Returns true if the list is empty, else false.

        Arguments:
        self -- reference to this list instance
        """
        pass

    def add_before(self, node, new):
        """Inserts a node containing new before a given node.

        Arguments:
        self -- reference to this list instance
        node -- the node before which new is inserted
        new -- data value for the new node
        """
        pass

    def add_after(self, node, new):
        """Inserts a node containing new after a given node.

        Arguments:
        self -- reference to this list instance
        node -- the node before which new is inserted
        new -- data value for the new node
        """
        pass
