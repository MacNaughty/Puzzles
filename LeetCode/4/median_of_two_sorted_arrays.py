import unittest
from typing import List


class Solution:

    @classmethod
    def get_medium_from_res(cls, res: List[int], len_res):
        if len_res % 2 == 1:
            return res[len_res // 2]
        else:
            return (res[len_res // 2] + res[(len_res // 2) - 1]) / 2

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        len_nums1 = len(nums1)
        len_nums2 = len(nums2)

        if len_nums1 == 0:
            return self.get_medium_from_res(nums2, len_nums2)

        if len_nums2 == 0:
            return self.get_medium_from_res(nums1, len_nums1)

        i = 0
        j = 0
        res = []
        while i < len_nums1 and j < len_nums2:
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                res.append(nums2[j])
                j += 1

        if i < len_nums1:
            res.extend(nums1[i:])

        if j < len_nums2:
            res.extend(nums2[j:])

        len_res = len(res)
        return self.get_medium_from_res(res, len_res)
    

class TestCase(unittest.TestCase):

    def test_1(self):
        nums1 = [1, 3]
        nums2 = [2]
        self.assertEqual(2, Solution().findMedianSortedArrays(nums1, nums2))

    def test_2(self):
        nums1 = [1, 2]
        nums2 = [3, 4]
        self.assertEqual(2.5, Solution().findMedianSortedArrays(nums1, nums2))

    def test_3(self):
        nums1 = [1, 1]
        nums2 = [1, 2]
        self.assertEqual(1, Solution().findMedianSortedArrays(nums1, nums2))


if __name__ == '__main__':
    unittest.main()
