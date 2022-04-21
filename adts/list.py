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
        new_node.next = self.head
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

            #Update the head pointer if there are other nodes
            if self.head.next != None:
                self.head = self.head.next
                #Remove the new head's pointer to the old one
                self.head.prev = None
            #Remove the head pointer if it is the only element
            else:
                self.head = None

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
        new_node.prev = self.tail
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
        """Removes the back item and returns its data.

        Arguments:
        self -- reference to this list instance
        """
        if self.tail != None:
            #Get the data from the old tail
            data = self.tail.data

            #Update the tail pointer if there are other nodes
            if self.tail.prev != None:
                self.tail = self.tail.prev
                #Remove the new tail's pointer to the old one
                self.tail.next = None
            #Remove the head and tail pointer if it is the only element
            else:
                self.head = None
                self.tail = None

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
        while node != None:
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
        while node != None and node.data != key:
            node = node.next

        #If the node data and key match remove the node and break
        if node.data == key:
            #Remove node from the list
            if node.prev == None:
                self.pop_front()
            elif node.next == None:
                self.pop_back()
            else:
                node.prev.next = node.next
                node.next.prev = node.prev

    def empty(self):
        """Returns true if the list is empty, else false.

        Arguments:
        self -- reference to this list instance
        """
        if self.head == None:
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
        new_node.prev = node.prev
        new_node.next = node
        #If node is head, use the push_front method
        if node.prev == None:
            self.push_front(new)
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
        new_node.prev = node
        new_node.next = node.next
        #If node is tail, use the push_back method
        if node.next == None:
            self.push_back(new)
        else:
            node.next.prev = new_node
            node.next = new_node

    def print_list(self):
        """Prints all elements in the list.

        Arguments:
        self -- reference to this list instance
        """
        node = self.head
        while node != None:
            print(node.data)
            node = node.next

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
    print("Current head: " + str(list.head.data))
    print("Current tail: " + str(list.tail.data))

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
    node = list.head
    while node.data != 4:
        node = node.next
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
