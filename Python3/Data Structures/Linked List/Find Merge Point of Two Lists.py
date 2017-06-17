"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def FindMergeNode(headA, headB):
    length_A = 0
    length_B = 0

    curr_node_A = headA
    curr_node_B = headB

    while curr_node_A:
        length_A += 1
        curr_node_A = curr_node_A.next

    while curr_node_B:
        length_B += 1
        curr_node_B = curr_node_B.next

    curr_node_A = headA
    curr_node_B = headB
    if length_A == length_B:
        while curr_node_A or curr_node_B:
            if curr_node_A.data == curr_node_B.data:
                result = curr_node_A.data
                return result
            else:
                curr_node_A = curr_node_A.next
                curr_node_B = curr_node_B.next

    elif length_A > length_B:
        curr_node_B = headB
        while curr_node_B:
            curr_node_A = headA
            while curr_node_A:
                if curr_node_A.data == curr_node_B.data:
                    result = curr_node_A.data
                    return result
                else:
                    curr_node_A = curr_node_A.next
            curr_node_B = curr_node_B.next

    else:
        curr_node_A = headA
        while curr_node_A:
            curr_node_B = headB
            while curr_node_B:
                if curr_node_A.data == curr_node_B.data:
                    result = curr_node_A.data
                    return result
                else:
                    curr_node_B = curr_node_B.next
            curr_node_A = curr_node_A.next
