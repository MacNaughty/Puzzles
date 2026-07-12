import heapq
import unittest
from math import inf
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])

        heap = [(0, 0, 0)] # (effort, i, j)
        dp = [[float('inf')] * n for _ in range(m)]
        dp[0][0] = 0

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        while heap:
            prev_effort, i, j = heapq.heappop(heap)
            if i == m - 1 and j == n - 1:
                return prev_effort

            for [di, dj] in directions:
                mi, nj = i + di, j + dj
                if 0 <= mi < m and 0 <= nj < n:
                    new_effort = max(prev_effort, abs(heights[i][j] - heights[mi][nj]))
                    if new_effort < dp[mi][nj]:
                        dp[mi][nj] = new_effort
                        heapq.heappush(heap, (new_effort, mi, nj))


class MyTestCase(unittest.TestCase):
    def test_1(self):
        heights = [[1,2,2],[3,8,2],[5,3,5]]
        expected = 2
        actual = Solution().minimumEffortPath(heights)
        self.assertEqual(expected, actual)

    def test_2(self):
        heights = [[1,2,3],[3,8,4],[5,3,5]]
        expected = 1
        actual = Solution().minimumEffortPath(heights)
        self.assertEqual(expected, actual)

    def test_3(self):
        heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
        expected = 0
        actual = Solution().minimumEffortPath(heights)
        self.assertEqual(expected, actual)

    def test_4(self):
        heights = [[1,10,6,7,9,10,4,9]]
        expected = 9
        actual = Solution().minimumEffortPath(heights)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
