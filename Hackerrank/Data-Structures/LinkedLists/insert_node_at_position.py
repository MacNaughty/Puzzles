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

def insertNodeAtPosition(llist, data, position):

    node = llist
    for i in range(position - 1):
        node = node.next

    next = node.next
    node.next = SinglyLinkedListNode(data)
    node.next.next = next

    return llist




if __name__ == '__main__':

    llist = SinglyLinkedList()
    llist.insert_node(16)
    llist.insert_node(13)
    llist.insert_node(7)

    insertNodeAtPosition(llist.head, 1, 2)
    print_singly_linked_list(llist.head, ' ')




