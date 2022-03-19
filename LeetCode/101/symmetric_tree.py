import unittest
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def are_nodes_same(self, left: Optional[TreeNode], right: Optional[TreeNode]):
        if left is None and right is None:
            return True
                
        if left is None or right is None:
            return False

        return left.val == right.val and self.are_nodes_same(left.right, right.left) and self.are_nodes_same(left.left, right.right)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.are_nodes_same(root.left, root.right)



class TestCase(unittest.TestCase):

    def test1_isSymmetric1(self):
        test_input = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
        self.assertEqual(True, Solution().isSymmetric(test_input))

    def test2_isSymmetric(self):
        test_input = TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(5)))
        self.assertEqual(False, Solution().isSymmetric(test_input))


if __name__ == '__main__':
    unittest.main()
