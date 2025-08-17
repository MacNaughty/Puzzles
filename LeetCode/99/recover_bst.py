# Definition for a binary tree node.
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    parent_to_swap: TreeNode|None = None
    child_to_swap: TreeNode|None = None

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """


class MyTestCase(unittest.TestCase):

    def my_testcase_helper(self, expected_node, actual_node):
        # Both are None, valid case
        if not expected_node and not actual_node:
            self.assertTrue(True)
            return

        # If one is None but the other is not
        if not expected_node or not actual_node:
            self.assertTrue(False, "One of the nodes is None while the other isn't")

        # Check the value of both nodes
        self.assertEqual(expected_node.val, actual_node.val, f"Values do not match: {expected_node.val} != {actual_node.val}")

        # Check left subtree recursively
        self.my_testcase_helper(expected_node.left, actual_node.left)

        # Check right subtree recursively
        self.my_testcase_helper(expected_node.right, actual_node.right)

    def test_1(self):
        root = TreeNode(1, TreeNode(3, None, TreeNode(2)))
        Solution().recoverTree(root)
        expected = TreeNode(3, TreeNode(1, None, TreeNode(2)))
        self.my_testcase_helper(expected, root)

    def test_2(self):
        root = TreeNode(3, TreeNode(1), TreeNode(4, TreeNode(2)))
        Solution().recoverTree(root)
        expected = TreeNode(2, TreeNode(1), TreeNode(4, TreeNode(3)))
        self.my_testcase_helper(expected, root)

    def test_3(self):
        root = TreeNode(2, TreeNode(3), TreeNode(1))
        Solution().recoverTree(root)
        expected = TreeNode(2, TreeNode(1), TreeNode(3))
        self.my_testcase_helper(expected, root)


if __name__ == '__main__':
    unittest.main()
