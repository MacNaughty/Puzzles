import unittest
from functools import reduce, lru_cache
from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        num_jobs = len(jobDifficulty)

        if d > num_jobs:
            return -1

        dp = [[float('inf')] * num_jobs for _ in range(d)]

        max_d = 0
        for i in range(num_jobs - d + 1):
            max_d = max(max_d, jobDifficulty[i])
            dp[0][i] = max_d

        for today in range(1, d):
            for t in range(today, num_jobs-d+today+1):
                t_diff = jobDifficulty[t]
                min_diff_t = float('inf')

                for j in range(t - 1, today - 2, -1):
                    min_diff_t = min(min_diff_t, dp[today-1][j] + t_diff)
                    t_diff = max(t_diff, jobDifficulty[j])

                dp[today][t] = min_diff_t

        return dp[d - 1][-1]

class MyTestCase(unittest.TestCase):
    def test_1(self):
        jobDifficulty = [6,5,4,3,2,1]
        d = 2
        expected = 7
        actual = Solution().minDifficulty(jobDifficulty, d)
        self.assertEqual(expected, actual)  # add assertion here

    def test_2(self):
        jobDifficulty = [9,9,9]
        d = 4
        expected = -1
        actual = Solution().minDifficulty(jobDifficulty, d)
        self.assertEqual(expected, actual)  # add assertion here

    def test_3(self):
        jobDifficulty = [1,1,1]
        d = 3
        expected = 3
        actual = Solution().minDifficulty(jobDifficulty, d)
        self.assertEqual(expected, actual)  # add assertion here

    def test_4(self):
        jobDifficulty = [11,111,22,222,33,333,44,444]
        d = 6
        expected = 843
        actual = Solution().minDifficulty(jobDifficulty, d)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
