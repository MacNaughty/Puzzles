"""
 Merge two linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def CompareLists(headA, headB):
    result = 1
    
    curr_node_A = headA
    curr_node_B = headB
    
    
    if not curr_node_A and curr_node_B:
        result = 0
    if curr_node_A and not curr_node_B:
        result = 0
    
    while curr_node_A and curr_node_B:
        if curr_node_A.data != curr_node_B.data:
            result = 0
            break
        else:
            curr_node_A = curr_node_A.next
            curr_node_B = curr_node_B.next

    if not curr_node_A and curr_node_B:
        result = 0
    if curr_node_A and not curr_node_B:
        result = 0

    return result
