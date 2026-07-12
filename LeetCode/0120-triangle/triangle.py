import unittest
from typing import List


class Solution:
    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    #     # for each level of the tree, track the minimum path to get there
    #
    #     for i in range(1, len(triangle)):
    #         for j in range(len(triangle[i])):
    #             if 0 < j < len(triangle[i]) - 1:
    #                 triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
    #             elif j == 0:
    #                 triangle[i][0] += triangle[i-1][0]
    #             else:
    #                 # j == len(acc) - 1
    #                 triangle[i][j] += triangle[i-1][j-1]
    #
    #     return min(triangle[-1])

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Initialize our DP array with the values of the very bottom row
        dp = triangle[-1][:]

        # Start from the second to last row and move upwards
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                # Update the dp array in place
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        return dp[0]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        input = [[2],[3,4],[6,5,7],[4,1,8,3]]
        expected = 11
        actual = Solution().minimumTotal(input)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
