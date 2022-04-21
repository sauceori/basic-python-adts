2022 SOFTWARE ENGINEERING INTERN CANDIDATE PROGRAMMING CHALLENGE
Ethan Hopkins for Durbin Group

INTRODUCTION
This project directory contains modules which implement abstract data types using the list, stack,
and queue data structures. In addition, unit and acceptance tests can be found within the tests
folder, and documentation for both the ADTs and tests can be found under the docs folder.
    The "adts" package contains modules representing the ADT implementations, and can be imported
into a working module in the parent directory using syntax such as "from adts.list import List."
list.py is an implementation of a doubly linked list, which was used as the underlying structure
for implementing the queue and stack ADTs as they conveniently share interface features with my
linked list.

DEVELOPMENT PROCESS
Starting out, I figured that I would write my list implementation first, since stacks and queues
can be easily implemented using linked lists that meant I could spend less time writing error-prone
code and more time testing the methods I write when creating the list ADT. I decided to go with a
doubly-linked list because having constant-time access to both the head and tail confers some
performance benefits, and makes writing certain methods easier even if it is more work having to
manage a tail reference.
    For each of the ADTs, I began by first creating the unit test stubs that would form my test
harness and correspond with the methods in my ADTs public interface. I documented each of these
stubs with the expectations for the method I would later implement as part of the corresponding ADT
and descriptions of the cases they represent, then I wrote the tests themselves. I then implemented
the ADT classes starting in the same way as with the tests: writing method stubs, documenting them,
and then implementing their expected behavior as established in the documentation. After creating
my list module, I wrote some "quick and dirty" tests in its main method which helped me to work out
some bugs and get my interface methods to better mesh with the test suite I had prepared for them.
When all the ADTs had been written and their tests came back ok, I wrote up some use-case scenarios
for the data structures to create acceptance tests that showcase as much of their functionality as
possible and added these tests to the end of the corresponding modules in the test package.
    I based the public interfaces of my ADTs on these three videos from UC San Diego on
linked-lists, stacks, and queues. I had recently seen these videos when I was brushing up on my
knowledge of data structures and implementing them in C, so they seemed like a good fit for this
challenge:
Lists:  https://www.coursera.org/lecture/data-structures/singly-linked-lists-kHhgK
Stacks: https://www.coursera.org/lecture/data-structures/stacks-UdKzQ
Queues: https://www.coursera.org/lecture/data-structures/queues-EShpq

TESTS
The tests package contains modules which correspond to the list, stack, and queue ADTs and contain
unit tests which check interface methods on an individual basis and acceptance tests which use
use-case scenarios to confirm more general functionality for these ADTs. These tests can all be run
sequentially using the test.sh shell script in the base of the project directory.

DOCUMENTATION
For this project I documented my code with pydoc docstrings, the documentation in .html formis
available in the docs directory in the root of the project folder and can be generated again if
changes are introduced by running the docs.sh script in the same location. I referenced the
following style guides for more general style and pydoc docstring conventions:
Style: https://peps.python.org/pep-0008/
Pydoc: https://peps.python.org/pep-0257/
