"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

# using recursion
# reminder: don't print anything if the linkedlist is null
# print the list from tail to head
def ReversePrint(head):
    curr_node = head
    if curr_node != None:
        ReversePrint(curr_node.next)
        print(curr_node.data)
