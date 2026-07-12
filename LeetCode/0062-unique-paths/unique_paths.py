import unittest
from collections import defaultdict


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        memo = defaultdict(int)
        def permute_paths(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            if (i, j) in memo:
                return memo[(i, j)]

            if i < m-1:
                memo[(i, j)] += permute_paths(i+1, j)
            if j < n-1:
                memo[(i, j)] += permute_paths(i, j+1)

            return memo[(i, j)]
        return permute_paths(0, 0)


    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * m  # Only need to initialize to 1 for the first row

        for i in range(1, n):  # Start from row 1
            for j in range(1, m):
                dp[j] += dp[j - 1]

        return dp[m - 1]




class MyTestCase(unittest.TestCase):
    def test_0(self):
        m = 2
        n = 2
        expected = 2
        actual = Solution().uniquePaths(m, n)
        self.assertEqual(expected, actual)  # add assertion here

    def test_1(self):
        m = 3
        n = 2
        expected = 3
        actual = Solution().uniquePaths(m, n)
        self.assertEqual(expected, actual)  # add assertion here

    def test_1_1(self):
        m = 2
        n = 3
        expected = 3
        actual = Solution().uniquePaths(m, n)
        self.assertEqual(expected, actual)  # add assertion here

    def test_2(self):
        m = 3
        n = 7
        expected = 28
        actual = Solution().uniquePaths(m, n)
        self.assertEqual(expected, actual)  # add assertion here

    def test_2_2(self):
        m = 7
        n = 3
        expected = 28
        actual = Solution().uniquePaths(m, n)
        self.assertEqual(expected, actual)  # add assertion here

    def test_3(self):
        m = 23
        n = 12
        expected = 193536720
        actual = Solution().uniquePaths(m, n)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
