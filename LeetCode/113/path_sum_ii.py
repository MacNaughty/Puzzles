import unittest
from typing import Optional, List

from util.test_helper import TreeNode, MyTestCaseHelper


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        result = []

        def dfs(node, path, total):
            if not node:
                return

            path.append(node.val)
            total += node.val

            # Check if it's a leaf node and sum matches
            if not node.left and not node.right and total == targetSum:
                result.append(path[:])

            dfs(node.left, path, total)
            dfs(node.right, path, total)
            path.pop()  # Backtrack

        dfs(root, [], 0)
        return result


class MyTestCase(unittest.TestCase):
    def test_1(self):
        root = MyTestCaseHelper().array_to_binary_tree([5,4,8,11,None,13,4,7,2,None,None,5,1])
        targetSum = 22
        expected = [[5,4,11,2],[5,8,4,5]]
        actual = Solution().pathSum(root, targetSum)
        self.assertEqual(expected, actual)

    def test_2(self):
        root = MyTestCaseHelper().array_to_binary_tree([1,2,3])
        targetSum = 5
        expected = []
        actual = Solution().pathSum(root, targetSum)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
