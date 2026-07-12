import unittest
from collections import defaultdict


class Solution:
    def uniquePaths(self, obstacleGrid) -> int:
        if 1 in {obstacleGrid[0][0], obstacleGrid[-1][-1]}:
            return 0

        memo = defaultdict(int)
        def permute_paths(i, j):
            if i < 0 or j < 0: return 0
            if i == 0 and j == 0: return 1

            if (i, j) not in memo:
                if obstacleGrid[i-1][j] != 1:
                    memo[(i, j)] += permute_paths(i-1, j)
                if obstacleGrid[i][j-1] != 1:
                    memo[(i, j)] += permute_paths(i, j-1)

            return memo[(i, j)]
        return permute_paths(len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1)



class MyTestCase(unittest.TestCase):
    def test_0(self):
        obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
        expected = 2
        actual = Solution().uniquePaths(obstacleGrid)
        self.assertEqual(expected, actual)  # add assertion here

    def test_1(self):
        obstacleGrid = [[0,1],[0,0]]
        expected = 1
        actual = Solution().uniquePaths(obstacleGrid)
        self.assertEqual(expected, actual)  # add assertion here

    def test_2(self):
        obstacleGrid = [[1]]
        expected = 0
        actual = Solution().uniquePaths(obstacleGrid)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
