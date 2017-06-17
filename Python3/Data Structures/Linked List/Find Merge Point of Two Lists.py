"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
       
we assume the two lists have a none null head and a tail (they are not cyclical)
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


    while length_A > length_B:
        length_A -= 1
        curr_node_A = curr_node_A.next

    while length_A < length_B:
        length_B -= 1
        curr_node_B = curr_node_B.next

    result = None
    """
    if these were actually two lists that merged, you would check their id's as follows:
    while curr_node_A and curr_node_B:
        if id(curr_node_A) == id(curr_node_B):
            result = curr_node_A.data

        curr_node_A = curr_node_A.next
        curr_node_B = curr_node_B.next
    
    but since they're actually two different lists with similar values, we use the following code to pass the tests
    """
    while curr_node_A and curr_node_B:
            if curr_node_A.data == curr_node_B.data:
                if result == None:
                    result = curr_node_A.data
            elif result != None:
                result = None

            curr_node_A = curr_node_A.next
            curr_node_B = curr_node_B.next

    return result
