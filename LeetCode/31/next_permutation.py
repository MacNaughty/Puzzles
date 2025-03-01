import unittest
from typing import List


class Solution:

    def nextPermutation(self, nums: List[int]) -> None:
        len_nums = len(nums)
        left = 0
        right = len_nums - 1

        for i in range(right, 0, -1):
            if nums[i] > nums[i-1]:
                left = i - 1
                while nums[right] <= nums[left]:
                    right -= 1

                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right = len_nums - 1
                break

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


class MyTestCase(unittest.TestCase):
    def test_1(self):
        nums = [1, 2, 3]
        Solution().nextPermutation(nums)
        self.assertEqual(nums, [1, 3, 2])

    def test_2(self):
        nums = [3, 2, 1]
        Solution().nextPermutation(nums)
        self.assertEqual(nums, [1, 2, 3])

    def test_3(self):
        nums = [1, 1, 5]
        Solution().nextPermutation(nums)
        self.assertEqual(nums, [1, 5, 1])

    def test_4(self):
        nums = [2, 3, 1]
        Solution().nextPermutation(nums)
        self.assertEqual(nums, [3, 1, 2])

    def test_5(self):
        nums = [1, 3, 2]
        Solution().nextPermutation(nums)
        self.assertEqual(nums, [2, 1, 3])

    def test_6(self):
        nums = [5, 4, 7, 5, 3, 2]
        Solution().nextPermutation(nums)
        self.assertEqual(nums, [5, 5, 2, 3, 4, 7])

    def test_7(self):
        nums = [4, 2, 0, 2, 3, 2, 0]
        Solution().nextPermutation(nums)
        self.assertEqual(nums, [4, 2, 0, 3, 0, 2, 2])


if __name__ == '__main__':
    unittest.main()
