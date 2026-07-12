import unittest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next

    return res

def assert_equal(node1, node2):
    linked_list1 = get_list(node1)
    linked_list2 = get_list(node2)
    print(f'linked_list1: {linked_list1}')
    print(f'linked_list2: {linked_list2}')

    if len(linked_list1) != len(linked_list2):
        return False

    for i in range(len(linked_list1)):
        if linked_list1[i] != linked_list2[i]:
            return False

    return True


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1 or not head.next:
            return head

        new_head = None
        last_tail = None
        node_list = [None] * k
        next_root = head
        while next_root:
            i = 0
            curr_node = next_root

            while i < k and curr_node:
                node_list[i] = curr_node
                curr_node = curr_node.next
                i += 1

            # we have a complete 'chunk' of k items
            if i != k:
                break

            next_root = curr_node
            if new_head is None:
                # this should only occur once; to return the result
                new_head = node_list[i-1]

            for j in range(i-1, 0, -1):
                node_list[j].next = node_list[j-1]
            if last_tail is not None:
                last_tail.next = node_list[i-1]
            last_tail = node_list[0]

        if last_tail is not None:
            last_tail.next = next_root

        return new_head


class MyTestCase(unittest.TestCase):
    def test_1(self):
        input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        output = ListNode(2, ListNode(1, ListNode(4, ListNode(3, ListNode(5)))))
        self.assertTrue(assert_equal(Solution().reverseKGroup(input, 2), output))

    def test_2(self):
        input = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
        output = ListNode(2, ListNode(1, ListNode(4, ListNode(3, ListNode(6, ListNode(5))))))
        self.assertTrue(assert_equal(Solution().reverseKGroup(input, 2), output))


if __name__ == '__main__':
    unittest.main()
