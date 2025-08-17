# Definition for a binary tree node.
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def is_node_valid(node, min_val, max_val):
            if not node:
                return True
            if not (min_val < node.val < max_val):
                return False

            return is_node_valid(node.left, min_val, node.val) and is_node_valid(node.right, node.val, max_val)

        return is_node_valid(root, -float('inf'), float('inf'))


class MyTestCase(unittest.TestCase):
    def test_0(self):
        expected = True
        actual = Solution().isValidBST(TreeNode(2, TreeNode(1), TreeNode(3)))
        self.assertEqual(expected, actual)

    def test_1(self):
        actual = Solution().isValidBST(TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6))))
        expected = False
        self.assertEqual(expected, actual)

    def test_2(self):
        actual = Solution().isValidBST(TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7))))
        expected = False
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
