import unittest
from typing import List


class Solution:
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     m, n = len(matrix), len(matrix[0])
    #
    #     # Binary search to find the correct row
    #     top, bottom = 0, m - 1
    #     row = -1
    #     while top <= bottom:
    #         mid = (top + bottom) // 2
    #         if target in {matrix[mid][0], matrix[mid][n - 1]}:
    #             return True
    #         if matrix[mid][0] < target < matrix[mid][n - 1]:
    #             row = mid
    #             break
    #         elif matrix[mid][0] > target:
    #             bottom = mid - 1
    #         else:
    #             top = mid + 1
    #
    #     if row == -1:
    #         return False
    #
    #     # Binary search within the row
    #     left, right = 0, n - 1
    #     while left <= right:
    #         mid = (left + right) // 2
    #         if matrix[row][mid] == target:
    #             return True
    #         elif matrix[row][mid] < target:
    #             left = mid + 1
    #         else:
    #             right = mid - 1
    #
    #     return False


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n
            mid_value = matrix[row][col]

            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False






class MyTestCase(unittest.TestCase):
    def test_1(self):
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        target = 3
        expected = True
        actual = Solution().searchMatrix(matrix, target)
        self.assertEqual(expected, actual)

    def test_2(self):
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        target = 13
        expected = False
        actual = Solution().searchMatrix(matrix, target)
        self.assertEqual(expected, actual)

    def test_3(self):
        matrix = [[1],[3],[5]]
        target = 5
        expected = True
        actual = Solution().searchMatrix(matrix, target)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
