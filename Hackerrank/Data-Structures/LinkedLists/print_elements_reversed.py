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

def reversePrint(llist):
    res = []
    while llist:
        res.append(llist.data)
        llist = llist.next

    for i in range(len(res)-1, -1, -1):
        print(res[i])



if __name__ == '__main__':

    llist = SinglyLinkedList()

    llist.insert_node(1)
    llist.insert_node(2)
    llist.insert_node(3)

    reversePrint(llist.head)
    # print_singly_linked_list(res, ' ')




