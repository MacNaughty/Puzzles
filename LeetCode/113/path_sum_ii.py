import unittest
from collections import deque
from typing import Optional, List

from util.test_helper import TreeNode, MyTestCaseHelper


class Solution:

    # def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
    #     if not root:
    #         return []
    #
    #     res = []
    #
    #     path = [root.val]
    #
    #     def check_path(path: list[int], curr_sum: int, curr: TreeNode):
    #         if curr_sum == targetSum and not (curr.left or curr.right):
    #             res.append(path[:])
    #             return
    #
    #         if not (curr.left or curr.right):
    #             return
    #
    #         if curr.left:
    #             path.append(curr.left.val)
    #             check_path(path, curr_sum + curr.left.val, curr.left)
    #
    #             path.pop()
    #
    #         if curr.right:
    #             path.append(curr.right.val)
    #             check_path(path, curr_sum + curr.right.val, curr.right)
    #             path.pop()
    #
    #     check_path(path, path[0], root)
    #
    #     return res

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def check_path(path: list[int], curr_sum: int, curr: TreeNode):
            if not curr: return

            curr_sum += curr.val
            path.append(curr.val)

            if curr_sum == targetSum and not (curr.left or curr.right):
                res.append(path[:])

            check_path(path, curr_sum, curr.left)
            check_path(path, curr_sum, curr.right)
            path.pop()

        check_path([], 0, root)

        return res



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

    def test_3(self):
        root = MyTestCaseHelper().array_to_binary_tree([1])
        targetSum = 1
        expected = [[1]]
        actual = Solution().pathSum(root, targetSum)
        self.assertEqual(expected, actual)

    def test_4(self):
        root = MyTestCaseHelper().array_to_binary_tree([1,-2,-3,1,3,-2,None,-1])
        targetSum = -1
        expected = [[1,-2,1,-1]]
        actual = Solution().pathSum(root, targetSum)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
