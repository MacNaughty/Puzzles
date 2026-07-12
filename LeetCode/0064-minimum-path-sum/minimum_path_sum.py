import unittest

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == n == 1:
            return grid[0][0]

        dp = [0]*n
        dp[0] = grid[0][0]

        for j in range(1, n):
            dp[j] = dp[j-1] + grid[0][j]

        for i in range(1, m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = grid[i][j] + min(dp[j], dp[j-1])

        return dp[-1]




class MyTestCase(unittest.TestCase):
    def test_1(self):
        grid = [[1,3,1],[1,5,1],[4,2,1]]
        expected = 7
        actual = Solution().minPathSum(grid)
        self.assertEqual(expected, actual)

    def test_2(self):
        grid = [[1,2,3],[4,5,6]]
        expected = 12
        actual = Solution().minPathSum(grid)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()