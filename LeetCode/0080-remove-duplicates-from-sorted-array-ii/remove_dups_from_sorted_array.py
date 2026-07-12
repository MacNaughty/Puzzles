import unittest
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)

        k = 2  # Start inserting from index 2
        for i in range(2, len(nums)):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
        return k


class MyTestCase(unittest.TestCase):
    def test_1(self):
        nums = [1,1,1,2,2,3]
        expected = 5
        actual = Solution().removeDuplicates(nums)
        self.assertEqual(expected, actual)
        self.assertEqual([1,1,2,2,3], nums[:actual])

    def test_2(self):
        nums = [0,0,1,1,1,1,2,3,3]
        expected = len([0,0,1,1,2,3,3])
        actual = Solution().removeDuplicates(nums)
        self.assertEqual(expected, actual)
        self.assertEqual([0,0,1,1,2,3,3], nums[:actual])

    def test_3(self):
        nums = [1,1,1]
        expected = len([1,1])
        actual = Solution().removeDuplicates(nums)
        self.assertEqual(expected, actual)
        self.assertEqual([1,1], nums[:actual])


if __name__ == '__main__':
    unittest.main()
