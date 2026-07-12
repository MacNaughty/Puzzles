import unittest
from typing import Optional

from util.test_helper import ListNode, MyTestCaseHelper


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy
        for i in range(left-1):
            prev = prev.next

        curr = prev.next
        for i in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next





class MyTestCase(unittest.TestCase):
    def test_1(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        left, right = 2, 4
        expected = [1,4,3,2,5]
        actual = Solution().reverseBetween(head, left, right)
        self.assertEqual(expected, MyTestCaseHelper().linked_list_to_array(actual))

    def test_2(self):
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
        left, right = 2, 5
        expected = [1,5,4,3,2,6]
        actual = Solution().reverseBetween(head, left, right)
        self.assertEqual(expected, MyTestCaseHelper().linked_list_to_array(actual))

if __name__ == '__main__':
    unittest.main()
