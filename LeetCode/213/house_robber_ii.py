import unittest
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return max(nums)

        def rob_linear(start, end):
            prev2, prev1, curr = 0, 0, 0

            for i in range(start, end):
                curr = max(nums[i] + prev2, prev1)
                prev2 = prev1
                prev1 = curr

            return prev1

        skip_first = rob_linear(1, n)
        skip_last = rob_linear(0, n-1)
        return max(skip_first, skip_last)

class MyTestCase(unittest.TestCase):
    def test_1(self):
        nums = [2,3,2]
        expected = 3
        actual = Solution().rob(nums)
        self.assertEqual(expected, actual)

    def test_2(self):
        nums = [1,2,3,1]
        expected = 4
        actual = Solution().rob(nums)
        self.assertEqual(expected, actual)

    def test_3(self):
        nums = [1,2,3]
        expected = 3
        actual = Solution().rob(nums)
        self.assertEqual(expected, actual)