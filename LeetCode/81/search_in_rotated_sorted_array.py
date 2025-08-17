import unittest
import bisect
from typing import List


class Solution:
    # def search(self, nums: List[int], target: int) -> bool:
    #     if nums[0] == target:
    #         return True
    #
    #     pivot_index = 0
    #     for i in range(1, len(nums)):
    #         if nums[i] == target:
    #             return True
    #         if nums[i] < nums[i-1]:
    #             pivot_index = i
    #             break
    #
    #     left = pivot_index + 1
    #     right = len(nums) - 1
    #     while left <= right:
    #         mid = (left + right) // 2
    #         if nums[mid] == target:
    #             return True
    #
    #         elif nums[mid] < target:
    #             left = mid + 1
    #         else:
    #             right = mid - 1
    #
    #     return False

    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            # If we can't determine which half is sorted
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            # Left half is sorted
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False



class MyTestCase(unittest.TestCase):
    def test_1(self):
        target = 0
        nums = [2,5,6,0,0,1,2]
        expected = True
        actual = Solution().search(nums, target)
        self.assertEqual(expected, actual)

    def test_2(self):
        target = 3
        nums = [2,5,6,0,0,1,2]
        expected = False
        actual = Solution().search(nums, target)
        self.assertEqual(expected, actual)

    def test_3(self):
        target = 0
        nums = [1,0,1,1,1]
        expected = True
        actual = Solution().search(nums, target)
        self.assertEqual(expected, actual)

    def test_4(self):
        target = 2
        nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1]
        expected = True
        actual = Solution().search(nums, target)
        self.assertEqual(expected, actual)

    def test_5(self):
        target = 2
        nums = [0,0,1,1,2,0]
        expected = True
        actual = Solution().search(nums, target)
        self.assertEqual(expected, actual)

    def test_6(self):
        target = 0
        nums = [2,2,2,0,1]
        expected = True
        actual = Solution().search(nums, target)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
