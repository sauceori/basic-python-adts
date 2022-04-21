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

PROJECT STRUCTURE
/adts/      Contains source modules for my ADT implementations
/docs/      Contains pydoc documentation for my ADTs and tests in .html format
/tests/     Contains modules with my unit and acceptance test cases for the ADTs
/docs.sh    Script which generates new documentation and places it in /docs/
/README.txt Contains information explaining my project
/test.sh    Script which runs test cases on my ADT modules

DEVELOPMENT PROCESS
Starting out, I figured that I would write my list implementation first, since stacks and queues
can be easily implemented using linked lists that meant I could spend less time writing potentially
error-prone code and more time testing the methods I write when creating the list ADT. I decided to
go with a doubly-linked list because having constant-time access to both the head and tail confers
some performance benefits, and makes writing certain methods easier even if it is more work having
to manage a tail reference.
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
    After writing all of my ADTs, ensuring they passed my test harness, and writing acceptance
tests for them I performed some code cleanup and other minor improvements. This included: improving
the encapsulation of the Node and List classes, updating my test suites to reflect these changes,
minor improvements to documentation and tests, and adding new comments where I noticed they were
lacking. Finally, I generated new .html docs to reflect the changed I had made.
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
    The acceptance test I wrote for my list ADT demonstrates how the list could be used to keep
track of families waiting in line with a FastPass system for an amusement park ride. I chose this
to be my example to showcase how the doubly linked list interface contrasts with stacks in queues,
particularly in the way that nodes can be inserted at the front, back, or in the middle of the
list (in the case that someone decides to leave the line.)
    For my Stack ADT my acceptance test shows how stacks are used in programs with "undo" features.
In my example, a very simple version control system allows its users to remove their most recent
changes if they are unhappy with them, popping the names of the edited files off of the stack.
    My queue ADT's acceptance test uses an automatic telemarketer as an example, numbers are fed to
the system and removed after it attempts the phone call. I thought this did a good job of
illustrating a use-case for FIFO priority structures, as the telemarketer simply attempts a call
for every number that it receives to maintain throughput.

DOCUMENTATION
For this project I documented my code with pydoc docstrings throughout, the documentation in .html
format is available in the docs directory in the root of the project folder and can be generated
again if changes are introduced by running the docs.sh script in the same location. I referenced
the following style guides for more general style and pydoc docstring conventions:
Style: https://peps.python.org/pep-0008/
Pydoc: https://peps.python.org/pep-0257/
