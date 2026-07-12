import unittest
from collections import defaultdict
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors_acc = defaultdict(int)
        for num in nums:
            colors_acc[num] += 1

        num_zeros = colors_acc[0]
        num_ones = colors_acc[1]
        # num_twos = colors_acc[2]

        for i in range(num_zeros):
            nums[i] = 0
        for i in range(num_zeros, num_zeros+num_ones):
            nums[i] = 1
        for i in range(num_zeros+num_ones, len(nums)):
            nums[i] = 2

    # Dutch National Flag algorithm
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid = 0, 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                if low != high:
                    nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

class MyTestCase(unittest.TestCase):
    def test_1(self):
        nums = [2,0,2,1,1,0]
        expected = [0,0,1,1,2,2]
        Solution().sortColors(nums)
        self.assertEqual(expected, nums)

    def test_2(self):
        nums = [2,0,1]
        expected = [0,1,2]
        Solution().sortColors(nums)
        self.assertEqual(expected, nums)


if __name__ == '__main__':
    unittest.main()
