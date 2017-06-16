"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""
# don't know how to traverse a singly linked list backwards (might be impossible)
#   so I'm just going to collect the elements in a deque with appendleft (push) 
#   and print them

from collections import deque
# print the list from tail to head
def ReversePrint(head):
    curr_node = head
    collect = deque()
    while curr_node != None:
        collect.appendleft(curr_node.data)
        curr_node = curr_node.next
    for data in collect:
        print(data)
