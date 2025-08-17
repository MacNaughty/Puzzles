import unittest
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], nums]

        nums.sort()

        res = []
        def build_subsets(path, start):
            res.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                build_subsets(path, i+1)
                path.pop()

        build_subsets([], 0)
        return res

class MyTestCase(unittest.TestCase):
    def test_1(self):
        nums = [1,2,2]
        expected = set([tuple(subset) for subset in [[],[1],[1,2],[1,2,2],[2],[2,2]]])
        actual = Solution().subsetsWithDup(nums)
        self.assertEqual(len(expected), len(actual))
        for s in actual:
            self.assertIn(tuple(s), expected)


if __name__ == '__main__':
    unittest.main()
