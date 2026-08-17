"""
List methods make it easy to use a list as a stack.

A stack follows the LIFO principle:
Last-In, First-Out.

To add an item to the top of the stack:
    use append()

To retrieve/remove the top item:
    use pop() without an index.
"""

from collections import deque


stack = [4,3,2,1] # create an empty list to use as a stack
stack.append(5) # add 5 to the top of the stack
print(stack) # prints the updated stack

stack.pop() # removes the top item (5) from the stack
print(stack) # prints the updated stack
#-----------------------------------------------------------------------------------------------

"""
List methods make it easy to use a list as a queue.

A queue follows the FIFO principle:
First-In, First-Out.

To add an item to the end of the queue:
    use append()

To retrieve/remove the first item:
    use pop(0).

To implement a queue, use collections.
deque which was designed to have fast appends and pops from both ends    
"""
from collections import deque
queue = deque([4,3,2,1]) # create an empty list to use as a queue
queue.append(5) # add 5 to the end of the queue
print(queue) # prints the updated queue

queue.popleft() # removes the first item (4) from the queue
print(queue) # prints the updated queue