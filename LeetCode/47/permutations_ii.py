import unittest
from typing import List

from util.test_helper import MyTestCaseHelper


class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def helper(path: list[int], used: list[bool]) -> None:
            if len(path) == len(nums):
                res.append(tuple(path))
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i-1] and used[i-1]:
                    continue

                path.append(nums[i])
                used[i] = True
                helper(path, used)
                path.pop()
                used[i] = False

        helper([], [False]*len(nums))
        return res


class MyTestCase(unittest.TestCase):
    def test_1(self):
        expected = [[1,1,2], [1,2,1], [2,1,1]]
        actual = Solution().permuteUnique([1,1,2])
        MyTestCaseHelper().assert_two_d_lists_equal(expected, actual)

    def test_2(self):
        expected = [[0, 3, 3, 3], [3, 0, 3, 3], [3, 3, 0, 3], [3, 3, 3, 0]]
        actual = Solution().permuteUnique([3, 3, 0, 3])
        MyTestCaseHelper().assert_two_d_lists_equal(expected, actual)

    def test_3(self):
        expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        actual = Solution().permuteUnique([1,2,3])
        MyTestCaseHelper().assert_two_d_lists_equal(expected, actual)


if __name__ == '__main__':
    unittest.main()
