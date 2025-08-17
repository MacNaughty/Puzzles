import unittest
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0] * len(nums)

        for i in range(len(nums)):
            if nums[i] == 0:
                break

            local_max = i + nums[i]

            for j in range(i, min(len(nums), i + local_max)):
                dp[j] = max(dp[j], i + local_max)

        return dp[j] >= len(nums) - 1


    def canJump(self, nums):
        max_reach = 0  # Track the farthest index we can reach

        for i, jump in enumerate(nums):
            if i > max_reach:
                return False  # If we reach an index we can't get to, return False
            max_reach = max(max_reach, i + jump)  # Update the farthest reachable index
            if max_reach >= len(nums) - 1:
                return True  # If we can reach the last index, return True

        return False  # If we exit the loop, we couldn't reach the last index




class MyTestCase(unittest.TestCase):
    def test_1(self):
        input = [2,3,1,1,4]
        expected = True
        actual = Solution().canJump(input)
        self.assertEqual(expected, actual)  # add assertion here

    def test_2(self):
        input = [3,2,1,0,4]
        expected = False
        actual = Solution().canJump(input)
        self.assertEqual(expected, actual)  # add assertion here

    def test_3(self):
        input = [0]
        expected = True
        actual = Solution().canJump(input)
        self.assertEqual(expected, actual)  # add assertion here

    def test_4(self):
        input = [1,2]
        expected = True
        actual = Solution().canJump(input)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
