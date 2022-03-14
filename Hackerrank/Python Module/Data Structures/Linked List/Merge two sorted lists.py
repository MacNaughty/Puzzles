"""
 Print elements of a linked list on console
 head input could be None as well for empty list
 Node is defined as
"""

#return back the head of the linked list in the below method.


class Node:
    def __init__(self):
        self.data = None # contains the data
        self.next = None # contains the reference to the next node


class linked_list:
    def __init__(self):
        self.cur_node = None

    def add_node(self, data):
        new_node = Node() # create a new node
        new_node.data = data
        new_node.next = self.cur_node # link the new node to the 'previous' node.
        self.cur_node = new_node #  set the current node to the new one.

    def list_print(self):
        node = self.cur_node # cant point to ll!
        while node:
            print(node.data)
            node = node.next


def MergeLists(headA, headB):
    result_head = Node()

    if not headA:
        return headB
    if not headB:
        return headA

    curr_node_A = headA
    curr_node_B = headB

    # since we've now checked that the both first nodes are not empty, we can compare the first data
    if curr_node_A.data <= curr_node_B.data:
        result_head = curr_node_A
        curr_node_A = curr_node_A.next
    else:
        result_head = curr_node_B
        curr_node_B = curr_node_B.next

    result_body = result_head
    while curr_node_A or curr_node_B:
        if curr_node_A == None:
            result_body.next = curr_node_B
            break
        elif curr_node_B == None:
            result_body.next = curr_node_A
            break
        if curr_node_A.data <= curr_node_B.data:
            result_body.next = curr_node_A
            curr_node_A = curr_node_A.next
        else:
            result_body.next = curr_node_B
            curr_node_B = curr_node_B.next
        result_body = result_body.next

    return result_head

test_cases_list = list(map(int, (input().split())))
for _ in range(test_cases_list[0]):
    number_of_elements_list_A = int(input())
    if number_of_elements_list_A != 0:
        input_list = list(map(int, input().split()))
        L_A = linked_list()
        for i in range(number_of_elements_list_A):
            L_A.add_node(input_list[number_of_elements_list_A - i - 1])

    number_of_elements_list_B = int(input())
    if number_of_elements_list_B != 0:
        input_list = list(map(int, input().split()))
        L_B = linked_list()
        for i in range(number_of_elements_list_B):
            L_B.add_node(input_list[number_of_elements_list_B - i - 1])

    MergeLists(L_B.cur_node, L_A.cur_node)
