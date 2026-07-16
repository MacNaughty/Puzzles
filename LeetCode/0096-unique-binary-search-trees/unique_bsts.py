# Definition for a binary tree node.
import unittest

class Solution:

    def numTrees(self, n: int) -> int:
        """
        Compute Catalan number for n
        """
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

    def test_3(self):
        actual = Solution().numTrees(4)
        expected = 14
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
