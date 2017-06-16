"""
2
4
1 2 3 4
5
2 3 4 5 6
"""



def Reverse(head):
    prev_node = None
    curr_node = head

    while curr_node:
        prev_node, curr_node.next, curr_node = curr_node, prev_node, curr_node.next
        # it is important to have the assignments in this order:
        #   from what I understand, the expression evaluates from right to left
        #   first: the variables on the RHS of the '=' are set
        #       curr_node.next = 2
        #       prev_node = None
        #       curr_node = 1
        #   then the assignments are performed:
        #       curr_node = curr_node.next = 2
        #       curr_node.next = prev_node = None
        #       prev_node = curr_node = 1
        # if swap the order on the LHS to:
        # prev_node, curr_node, curr_node.next = curr_node, curr_node.next, prev_node
        #  File "solution.py", line 56, in Reverse
        # prev_node, curr_node, curr_node.next = curr_node, curr_node.next, prev_node
        #   AttributeError: 'NoneType' object has no attribute 'next'

    return prev_node
