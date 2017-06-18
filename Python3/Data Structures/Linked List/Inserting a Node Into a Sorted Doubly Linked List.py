"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as
"""
def insert_first(head, curr_node, data):
    if data > curr_node.data:
        new_node = Node(data, None, curr_node)
        curr_node.next = new_node
        head.next = curr_node
    else:
        new_node = Node(data, curr_node, None)
        curr_node.prev = new_node
        head.next = new_node

def insert_middle(prev_node, curr_node, data):
    new_node = Node(data, curr_node, prev_node)
    curr_node.prev = new_node
    prev_node.next = new_node

def insert_end(curr_node, data):
    new_node = Node(data, None, curr_node)
    curr_node.next = new_node

class Node(object):
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node  # contains the reference to the next node



    def SortedInsert(head, data):
    # base case: list is empty

        if not head.next:
            curr_node = Node(data, None)
            head.next = curr_node
            return head
    
    
            # else
        curr_node = head
        curr_node = curr_node.next
        prev_node = curr_node
        head.next = prev_node
        curr_node = curr_node.next
    
        if not prev_node.next:
            insert_first(head, prev_node, data)
            return head
    
        while curr_node:
            if curr_node.data >= data and prev_node.data <= data:
                insert_middle(prev_node, curr_node, data)
                break
            elif curr_node.next:
                curr_node = curr_node.next
                prev_node = prev_node.next
            else:
                insert_end(curr_node, data)
                break
    
        return head

#return the head node of the updated list



test_cases_list = list(map(int, (input().split())))
for _ in range(test_cases_list[0]):
    number_of_elements_list_A = int(input())
    if number_of_elements_list_A != 0:
        input_list = list(map(int, input().split()))
        head = Node()
        for element in input_list:
            head.SortedInsert(element)
