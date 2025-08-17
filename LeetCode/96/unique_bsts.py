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
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1  # Base case: 1 BST for 0 or 1 node

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]

        return dp[n]
    

class MyTestCase(unittest.TestCase):

    def test_0(self):
        actual = Solution().numTrees(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_1(self):
        actual = Solution().numTrees(2)
        expected = 2
        self.assertEqual(actual, expected)

    def test_2(self):
        actual = Solution().numTrees(3)
        expected = 5
        self.assertEqual(actual, expected)



        # for tree in actual:

        # self.assertEqual(, )  # add assertion here


if __name__ == '__main__':
    unittest.main()
