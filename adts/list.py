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
        #Node to be added to the list
        new_node = Node(new)
        #If the list is empty, then this is the first node
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        #Else new node becomes prev to current head, then the new head
        else:
            self.head.prev = new_node
            self.head = new_node

    def top_front(self):
        """Returns the value at the front of the list.

        Arguments:
        self -- reference to this list instance
        """
        if self.head != None:
            return self.head.data

    def pop_front(self):
        """Removes the head and returns its data.

        Arguments:
        self -- reference to this list instance
        """
        if self.head != None:
            #Get the data from the old head
            data = self.head.data

            #Update the head pointer
            self.head = self.head.next

            #Remove the new head's pointer to the old one
            self.head.prev = None

            #Return the old head data
            return data

    def push_back(self, new):
        """Adds a new node at the back of the list, replacing the tail node.

        Arguments:
        self -- reference to this list instance
        new -- data value for the new node
        """
        #Node to be added to the list
        new_node = Node(new)
        #If the list is empty, then this is the first node
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        #Else new node becomes next to current tail, then new tail
        else:
            self.tail.next = new_node
            self.tail = new_node

    def top_back(self):
        """Returns the value at the end of the list.

        Arguments:
        self -- reference to this list instance
        """
        if self.tail != None:
            return self.tail.data

    def pop_back(self):
        """Removes the front item and returns its data.

        Arguments:
        self -- reference to this list instance
        """
        if self.tail != None:
            #Get the data from the old tail
            data = self.tail.data

            #Update the tail pointer
            self.tail = self.tail.prev

            #Remove the new tail's pointer to the old one
            self.tail.next == None

            #Return the old tail data
            return data

    def find(self, key):
        """Returns true if the key is in the list, else false.

        Arguments:
        self -- reference to this list instance
        key -- the value to be searched for in the list
        """
        #Iterate through the linked list to find key
        node = self.head
        while node.next != None:
            #If the node data and key match return true
            if node.data == key:
                return True
            node = node.next
        #If the key is never found in the list return false
        return False

    def erase(self, key):
        """Removes the first instance of the key fron the list, if it exists.

        Arguments:
        self -- reference to this list instance
        key -- the value to be removed from the list
        """
        #Iterate through the linked list to find key
        node = self.head
        while node.next != None:
            #If the node data and key match remove the node and break
            if node.data == key:
                #Remove node from the list
                node.prev.next = node.next
                node.next.prev = node.prev
            node = node.next

    def empty(self):
        """Returns true if the list is empty, else false.

        Arguments:
        self -- reference to this list instance
        """
        if self.head == None:
            return True

    def add_before(self, node, new):
        """Inserts a node containing new before a given node.

        Arguments:
        self -- reference to this list instance
        node -- the node before which new is inserted
        new -- data value for the new node
        """
        #New node to be inserted
        new_node = Node(new)
        #If node is head, use the push_front method
        if node.prev == None:
            push_front(new)
        else:
            node.prev.next = new_node
            node.prev = new_node

    def add_after(self, node, new):
        """Inserts a node containing new after a given node.

        Arguments:
        self -- reference to this list instance
        node -- the node before which new is inserted
        new -- data value for the new node
        """
        #New node to be inserted
        new_node = Node(new)
        #If node is tail, use the push_back method
        if node.next == None:
            push_back(new)
        else:
            node.next.prev = new_node
            node.next = new_node
