import os


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep):
    res = ''
    while node:
        res += str(node.data)

        node = node.next

        if node:
            res += sep

    print(res)

def deleteNode(llist, position):

    if position == 0:
        return llist.next

    node = llist
    for i in range(position-1):
        node = node.next

    node.next = node.next.next

    return llist




if __name__ == '__main__':

    llist = SinglyLinkedList()

    llist.insert_node(11)
    llist.insert_node(12)
    llist.insert_node(8)
    llist.insert_node(18)
    llist.insert_node(16)
    llist.insert_node(5)
    llist.insert_node(18)

    res = deleteNode(llist.head, 6)
    print_singly_linked_list(res, ' ')




