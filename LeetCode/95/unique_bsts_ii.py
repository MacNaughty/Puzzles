# Definition for a binary tree node.
import unittest

from util.test_helper import MyTestCaseHelper


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def helper(start, end):
            if start > end:
                return [None]

            all_trees = []
            for i in range(start, end+1):

                left_trees = helper(start, i - 1)
                right_trees = helper(i + 1, end)

                for left_tree in left_trees:
                    for right_tree in right_trees:
                        curr_node = TreeNode(i)
                        curr_node.left = left_tree
                        curr_node.right = right_tree
                        all_trees.append(curr_node)

            return all_trees

        return helper(1, n)

class MyTestCase(unittest.TestCase):

    def test_0(self):
        actual = Solution().generateTrees(1)
        expected = [[1]]
        self.assertEqual(len(actual), len(expected))
        for i in range(len(expected)):
            MyTestCaseHelper().assert_expected_list_contains_tree(expected[i], actual[i])


    def test_1(self):
        actual = Solution().generateTrees(3)
        expected = [[1,None,2,None,3],[1,None,3,2],[2,1,3],[3,1,None,None,2],[3,2,None,1]]
        self.assertEqual(len(actual), len(expected))
        for i in range(len(expected)):
            MyTestCaseHelper().assert_expected_list_contains_tree(expected[i], actual[i])



        # for tree in actual:

        # self.assertEqual(, )  # add assertion here


if __name__ == '__main__':
    unittest.main()
