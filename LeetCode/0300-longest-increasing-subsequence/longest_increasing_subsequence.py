import unittest
from bisect import bisect_left
from typing import List


class Solution:
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     dp = [1] * n
    #
    #     prev_max = nums[0]
    #     max_streak = 1
    #     for i in range(1, n):
    #         if nums[i] > nums[i-1]:
    #             if prev_max > nums[i]:
    #                 dp[i] = 1 + dp[i-1]
    #             elif prev_max == nums[i]:
    #                 max_streak = max(max_streak, dp[i-1]+1)
    #                 dp[i] = max_streak
    #             elif prev_max < nums[i]:
    #                 prev_max = nums[i]
    #                 max_streak += 1
    #                 dp[i] = max_streak
    #
    #     return max(dp)

    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     dp = [1] * n
    #
    #     for i in range(1, n):
    #         for j in range(i):
    #             if nums[i] > nums[j]:
    #                 dp[i] = max(dp[i], dp[j]+1)
    #
    #     return max(dp)

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        sub = [nums[0]]

        for i in range(1, n):
            if nums[i] > sub[-1]:
                sub.append(nums[i])
            else:
                idx = bisect_left(sub, nums[i])
                sub[idx] = nums[i]

        return len(sub)


class MyTestCase(unittest.TestCase):
    def test_1(self):
        nums = [10, 9, 2, 5, 3, 7, 101, 18]
        expected = 4
        actual = Solution().lengthOfLIS(nums)
        self.assertEqual(expected, actual)

    def test_2(self):
        nums = [0,1,0,3,2,3]
        expected = 4
        actual = Solution().lengthOfLIS(nums)
        self.assertEqual(expected, actual)

    def test_3(self):
        nums = [7,7,7,7,7,7,7]
        expected = 1
        actual = Solution().lengthOfLIS(nums)
        self.assertEqual(expected, actual)

    def test_4(self):
        nums = [5, 4, 3, 2]
        expected = 1
        actual = Solution().lengthOfLIS(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
