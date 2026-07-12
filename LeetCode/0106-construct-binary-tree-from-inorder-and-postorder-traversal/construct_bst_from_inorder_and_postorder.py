import unittest
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Create a map to store the index of each value in inorder for quick lookup
        inorder_map = {v: i for i, v in enumerate(inorder)}

        # Start from the last index of postorder (root of the tree)
        postorder_index = len(postorder) - 1

        def construct_bst(left, right):
            nonlocal postorder_index
            # Base case: if left > right, no elements to construct
            if left > right:
                return None

            # Get the current root from postorder
            postorder_val = postorder[postorder_index]
            postorder_index -= 1

            # Create the root node
            root = TreeNode(postorder_val)

            root_index = inorder_map[postorder_val]

            root.right = construct_bst(root_index+1, right)
            root.left = construct_bst(left, root_index-1)

            return root

        return construct_bst(0, len(postorder) - 1)

class MyTestCase(unittest.TestCase):
    def test_1(self):
        inorder = [9,3,15,20,7]
        postorder = [9,15,7,20,3]
        self.assertTrue(Solution().buildTree(inorder, postorder))  # add assertion here


if __name__ == '__main__':
    unittest.main()
