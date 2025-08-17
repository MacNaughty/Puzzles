import unittest
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        jumps = furthest = curr_end = 0
        for i in range(len(nums) - 1):
            furthest = max(furthest, i + nums[i])

            if i == curr_end:
                jumps += 1
                curr_end = furthest

                if curr_end >= len(nums)-1:
                    break

        return jumps

class MyTestCase(unittest.TestCase):
    def test_1(self):
        actual = Solution().jump([2, 3, 1, 1, 4])

        self.assertEqual(2, actual)  # add assertion here

    def test_2(self):
        actual = Solution().jump([2, 3, 0, 1, 4])

        self.assertEqual(2, actual)  # add assertion here

    def test_3(self):
        actual = Solution().jump([1, 1, 2, 1, 4])

        self.assertEqual(3, actual)  # add assertion here

    def test_4(self):
        actual = Solution().jump([1, 2, 1, 5, 1, 1, 1, 1, 1])

        self.assertEqual(3, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
