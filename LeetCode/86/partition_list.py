import unittest
from typing import Optional

from util.test_helper import ListNode, MyTestCaseHelper


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None

        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)
        less = less_dummy
        greater = greater_dummy
        curr = head

        while curr:
            if curr.val < x:
                less.next = curr
                less = less.next
            else:
                greater.next = curr
                greater = greater.next
            curr = curr.next

        greater.next = None
        less.next = greater_dummy.next
        return less_dummy.next


class MyTestCase(unittest.TestCase):
    def test_0(self):
        head = ListNode(1)
        x = 2
        expected = [1]
        actual = Solution().partition(head, x)
        actual = MyTestCaseHelper().linked_list_to_array(actual)
        self.assertEqual(expected, actual)

    def test_1(self):
        head = ListNode(1, ListNode(4,ListNode(3,ListNode(2,ListNode(5,ListNode(2))))))
        x = 3
        expected = [1,2,2,4,3,5]
        actual = Solution().partition(head, x)
        actual = MyTestCaseHelper().linked_list_to_array(actual)
        self.assertEqual(expected, actual)

    def test_2(self):
        head = ListNode(2, ListNode(1))
        x = 2
        expected = [1,2]
        actual = Solution().partition(head, x)
        actual = MyTestCaseHelper().linked_list_to_array(actual)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
