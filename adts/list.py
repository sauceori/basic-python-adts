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
        self._data = data
        self._prev = None
        self._next = None

    def get_data(self):
        """Accessor for the internal data variable.

        Arguments:
        self -- reference to this node instance
        """
        return self._data

    def set_data(self, new):
        """Mutator for the internal data variable.

        Arguments:
        self -- reference to this node instance
        new -- new value to be assigned to data
        """
        self._data = new

    def get_prev(self):
        """Accessor for the internal prev variable.

        Arguments:
        self -- reference to this node instance
        """
        return self._prev

    def set_prev(self, new):
        """Mutator for the internal prev variable.

        Arguments:
        self -- reference to this node instance
        new -- new value to be assigned to prev
        """
        self._prev = new

    def get_next(self):
        """Accessor for the internal next variable.

        Arguments:
        self -- reference to this node instance
        """
        return self._next

    def set_next(self, new):
        """Mutator for the internal next variable.

        Arguments:
        self -- reference to this node instance
        new -- new value to be assigned to next
        """
        self._next = new

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
        self._head = None
        self._tail = None

    def get_head(self):
        """Accessor for the head of the linked list.

        Arguments:
        self -- reference to this list instance
        """
        return self._head

    def get_tail(self):
        """Accessor for the tail of the linked list.

        Arguments:
        self -- reference to this list instance
        """
        return self._tail

    def push_front(self, new):
        """Adds a new node at the front of the list, replacing the head node.

        Arguments:
        self -- reference to this list instance
        new -- data value for the new node
        """
        #Node to be added to the list
        new_node = Node(new)
        new_node.set_next(self._head)
        #If the list is empty, then this is the first node
        if self._head == None:
            self._head = new_node
            self._tail = new_node
        #Else new node becomes prev to current head, then the new head
        else:
            self._head.set_prev(new_node)
            self._head = new_node

    def top_front(self):
        """Returns the value at the front of the list.

        Arguments:
        self -- reference to this list instance
        """
        if self._head != None:
            return self._head.get_data()

    def pop_front(self):
        """Removes the head and returns its data.

        Arguments:
        self -- reference to this list instance
        """
        if self._head != None:
            #Get the data from the old head
            data = self._head.get_data()

            #Update the head pointer if there are other nodes
            if self._head.get_next() != None:
                self._head = self._head.get_next()
                #Remove the new head's pointer to the old one
                self._head.set_prev(None)
            #Remove the head pointer if it is the only element
            else:
                self._head = None

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
        new_node.set_prev(self._tail)
        #If the list is empty, then this is the first node
        if self._head == None:
            self._head = new_node
            self._tail = new_node
        #Else new node becomes next to current tail, then new tail
        else:
            self._tail.set_next(new_node)
            self._tail = new_node

    def top_back(self):
        """Returns the value at the end of the list.

        Arguments:
        self -- reference to this list instance
        """
        if self._tail != None:
            return self._tail.get_data()

    def pop_back(self):
        """Removes the back item and returns its data.

        Arguments:
        self -- reference to this list instance
        """
        if self._tail != None:
            #Get the data from the old tail
            data = self._tail.get_data()

            #Update the tail pointer if there are other nodes
            if self._tail.get_prev() != None:
                self._tail = self._tail.get_prev()
                #Remove the new tail's pointer to the old one
                self._tail.set_next(None)
            #Remove the head and tail pointer if it is the only element
            else:
                self._head = None
                self._tail = None

            #Return the old tail data
            return data

    def find(self, key):
        """Returns true if the key is in the list, else false.

        Arguments:
        self -- reference to this list instance
        key -- the value to be searched for in the list
        """
        #Iterate through the linked list to find key
        node = self._head
        while node != None:
            #If the node data and key match return true
            if node.get_data() == key:
                return True
            node = node.get_next()
        #If the key is never found in the list return false
        return False

    def erase(self, key):
        """Removes the first instance of the key fron the list, if it exists.

        Arguments:
        self -- reference to this list instance
        key -- the value to be removed from the list
        """
        #Iterate through the linked list to find key
        node = self._head
        while node != None and node.get_data() != key:
            node = node.get_next()

        #If the node data and key match remove the node and break
        if node.get_data() == key:
            #Remove node from the list
            if node.get_prev() == None:
                self.pop_front()
            elif node.get_next() == None:
                self.pop_back()
            else:
                node.get_prev().set_next(node.get_next())
                #node.prev.next = node.next
                node.get_next().set_prev(node.get_prev())
                #node.next.prev = node.prev

    def empty(self):
        """Returns true if the list is empty, else false.

        Arguments:
        self -- reference to this list instance
        """
        if self._head == None:
            return True
        return False

    def add_before(self, node, new):
        """Inserts a node containing new before a given node.

        Arguments:
        self -- reference to this list instance
        node -- the node before which new is inserted
        new -- data value for the new node
        """
        #New node to be inserted
        new_node = Node(new)
        new_node.set_prev(node.get_prev())
        new_node.set_next(node)
        #If node is head, use the push_front method
        if node.get_prev() == None:
            self.push_front(new)
        else:
            node.get_prev().set_next(new_node)
            #node.prev.next = new_node
            node.set_prev(new_node)
            #node.prev = new_node

    def add_after(self, node, new):
        """Inserts a node containing new after a given node.

        Arguments:
        self -- reference to this list instance
        node -- the node before which new is inserted
        new -- data value for the new node
        """
        #New node to be inserted
        new_node = Node(new)
        new_node.set_prev(node)
        new_node.set_next(node.get_next())
        #If node is tail, use the push_back method
        if node.get_next() == None:
            self.push_back(new)
        else:
            node.get_next().set_prev(new_node)
            #node.next.prev = new_node
            node.set_next(new_node)
            #node.next = new_node

    def print_list(self):
        """Prints all elements in the list.

        Arguments:
        self -- reference to this list instance
        """
        node = self._head
        while node != None:
            print(node.get_data())
            node = node.get_next()

def main():
    """Contains "quick and dirty" checks for the list ADT."""

    #List for the method checks
    list = List()
    print("List created.")

    #empty should return true as nothing has been added to the list
    if(list.empty() == True):
        print("Empty works!")

    #Test push_front
    for x in range(6):
        list.push_front(x)
    list.print_list()

    #Test top_front
    if list.top_front() == 5:
        print("top_front works!")

    #Test pop_front
    if list.pop_front() == 5:
        list.print_list()
        print("pop_front works!")

    list = List()

    #Test push_back
    for x in range(6):
        list.push_back(x)
    list.print_list()

    #Test top_back
    if list.top_back() == 5:
        print("top_back works!")

    #Check head and tail
    print("Current head: " + str(list._head.get_data()))
    print("Current tail: " + str(list._tail.get_data()))

    #Test pop_back
    if list.pop_back() == 5:
        list.print_list()
        print("pop_back works!")

    #Test find
    if list.find(3) is True and list.find(5) is False:
        print("find works!")

    #Test erase
    list.erase(3)
    if list.find(3) is False:
        list.print_list()
        print("erase works!")

    #Test add_before
    node = list._head
    while node.get_data() != 4:
        node = node.get_next()
    list.add_before(node, 3)
    list.print_list()
    print("add_before works!")

    #Test add_after
    list.add_after(node, 5)
    list.add_after(node, 4.5)
    list.print_list()
    print("add_after works!")

#Run the checks
#main()
