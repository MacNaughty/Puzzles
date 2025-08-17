import unittest
from typing import Optional, List
from util.test_helper import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        curr_nodes = [root]
        is_left_start = True
        while curr_nodes:
            next_nodes = []
            curr_res = []

            indices = range(0, len(curr_nodes), 1) if is_left_start else range(len(curr_nodes)-1, -1, -1)

            for i in indices:
                curr = curr_nodes[i]
                curr_res.append(curr.val)
                if curr.left:
                    next_nodes.append(curr.left)
                if curr.right:
                    next_nodes.append(curr.right)

            res.append(curr_res)
            curr_nodes = next_nodes
            is_left_start = not is_left_start

        return res






class MyTestCase(unittest.TestCase):
    def test_1(self):
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        expected = [[3],[20,9],[15,7]]
        actual = Solution().zigzagLevelOrder(root)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
