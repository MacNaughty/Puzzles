# Definition for singly-linked list.
import unittest
from typing import Optional

from util.test_helper import MyTestCaseHelper


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next: return head

        num_nodes = 1
        prev_tail = head

        while prev_tail and prev_tail.next:
            num_nodes += 1
            prev_tail = prev_tail.next

        k %= num_nodes
        if k == 0: return head

        new_tail = head
        for _ in range(num_nodes - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        prev_tail.next = head

        return new_head

class MyTestCase(unittest.TestCase):

    def test_0(self):
        head = ListNode(1, ListNode(2))
        k = 1
        actual = Solution().rotateRight(head, k)
        MyTestCaseHelper().assert_list_nodes_equal(ListNode(2, ListNode(1)), actual)

    def test_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        k = 2
        actual = Solution().rotateRight(head, k)
        MyTestCaseHelper().assert_list_nodes_equal(ListNode(4, ListNode(5, ListNode(1, ListNode(2, ListNode(3))))), actual)