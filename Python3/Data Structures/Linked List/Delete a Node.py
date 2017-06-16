"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Delete(head, position):
    curr_node = head
    if position == 0:
        head = head.next
        return head
    else:
        for i in range(position + 1):
            next_node = curr_node.next
            if i == position:
                last_node.next = next_node
            else:
                last_node = curr_node
                curr_node = curr_node.next
        return head
