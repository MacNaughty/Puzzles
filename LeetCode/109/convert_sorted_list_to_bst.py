import unittest
from typing import Optional

from util.test_helper import ListNode, TreeNode, MyTestCaseHelper


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        curr = head
        num_nodes = 0
        node_list = []
        while curr:
            node_list.append(curr.val)
            curr = curr.next

        def build_children(left, right):
            if left > right:
                return

            mid = (left + right) // 2
            if node_list[mid] == '#':
                return

            curr = TreeNode(node_list[mid])
            node_list[mid] = '#'

            curr.left = build_children(left, mid-1)
            curr.right = build_children(mid+1, right)
            return curr

        tree_head = build_children(0, num_nodes -1)
        return tree_head










class MyTestCase(unittest.TestCase):
    def test_1(self):
        head = ListNode(-10,ListNode(-3,ListNode(0,ListNode(5,ListNode(9)))))
        expected = TreeNode(0, TreeNode(-3, TreeNode(-10)), TreeNode(9, TreeNode(5)))
        actual = Solution().sortedListToBST(head)
        self.assertEqual(MyTestCaseHelper().tree_to_list(expected), MyTestCaseHelper().tree_to_list(actual))


if __name__ == '__main__':
    unittest.main()
