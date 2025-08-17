import unittest
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])

        res = []

        top, bottom, left, right = 0, m - 1, 0, n - 1

        while top <= bottom and left <= right:

            # Traverse from left to right along the top row
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1

            # Traverse from top to bottom along the right column
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            # Check if there are still rows and columns left
            if top <= bottom:
                # Traverse from right to left along the bottom row
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1

            if left <= right:
                # Traverse from bottom to top along the left column
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res


class MyTestCase(unittest.TestCase):
    def test_1(self):
        input = [[1,2,3],[4,5,6],[7,8,9]]
        expected = [1,2,3,6,9,8,7,4,5]
        actual = Solution().spiralOrder(input)
        self.assertEqual(expected, actual)  # add assertion here

    def test_2(self):
        input = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
        expected = [1,2,3,4,8,12,11,10,9,5,6,7]
        actual = Solution().spiralOrder(input)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
