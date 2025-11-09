import unittest
from typing import Optional

from util.test_helper import MyTestCaseHelper


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # TODO: much better solution leveraging sorted list input
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        dups = set()
        seen = set()

        curr = head
        while curr:
            if curr.val in seen:
                dups.add(curr.val)
            seen.add(curr.val)
            curr = curr.next

        while head and head.val in dups:
            head = head.next

        prev = head
        if head:
            curr = head.next
        while curr:
            while curr and curr.val in dups:
                curr = curr.next

            prev.next = curr
            prev = curr
            if curr:
                curr = curr.next

        return head


class MyTestCase(MyTestCaseHelper):
    def test_1(self):
        input_head = self.array_to_linked_list([1, 1, 1, 2, 3])
        expected = self.array_to_linked_list([2, 3])
        actual = Solution().deleteDuplicates(input_head)
        self.assert_list_nodes_equal(expected, actual)

    def test_2(self):
        input_head = self.array_to_linked_list([1,2,3,3,4,4,5])
        expected = self.array_to_linked_list([1,2,5])
        actual = Solution().deleteDuplicates(input_head)
        self.assert_list_nodes_equal(expected, actual)

if __name__ == '__main__':
    unittest.main()
