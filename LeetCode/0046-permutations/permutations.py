import unittest
from typing import List

from util.test_helper import MyTestCaseHelper


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(tuple(path))
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                path.append(nums[i])
                used[i] = True

                backtrack(path, used)
                path.pop()
                used[i] = False

        backtrack([], [False]*len(nums))
        return res

class MyTestCase(unittest.TestCase):
    def test_1(self):
        expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        actual = Solution().permute([1,2,3])
        MyTestCaseHelper().assert_two_d_lists_equal(expected, actual)

    def test_2(self):
        expected = [[0,1],[1,0]]
        actual = Solution().permute([0,1])
        MyTestCaseHelper().assert_two_d_lists_equal(expected, actual)

    def test_3(self):
        expected = [[1]]
        actual = Solution().permute([1])
        MyTestCaseHelper().assert_two_d_lists_equal(expected, actual)


if __name__ == '__main__':
    unittest.main()
