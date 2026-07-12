
import unittest
from typing import Optional

from util.test_helper import MyTestCaseHelper

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def generateTrees(self, n: int) -> list[Optional[TreeNode]]:
        if n == 1:
            return [TreeNode(1)]




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


if __name__ == '__main__':
    unittest.main()
