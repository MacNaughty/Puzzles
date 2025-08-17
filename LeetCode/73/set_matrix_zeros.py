import unittest
from typing import List


class Solution:
    def generateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        zero_rows = set()
        zero_cols = set()
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    zero_rows.add(row)
                    zero_cols.add(col)

        for row in zero_rows:
            for col in range(len(matrix[0])):
                matrix[row][col] = 0

        for col in zero_cols:
            for row in range(len(matrix)):
                matrix[row][col] = 0

        return matrix


class MyTestCase(unittest.TestCase):
    def test_1(self):
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        expected = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        actual = Solution().generateMatrix(matrix)
        self.assertEqual(expected, actual)

    def test_2(self):
        matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        expected = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
        actual = Solution().generateMatrix(matrix)
        self.assertEqual(expected, actual)

    def test_3(self):
        matrix = [[0, 0, 0, 5], [4, 3, 1, 4], [0, 1, 1, 4], [1, 2, 1, 3], [0, 0, 1, 1]]
        expected = [[0, 0, 0, 0], [0, 0, 0, 4], [0, 0, 0, 0], [0, 0, 0, 3], [0, 0, 0, 0]]
        actual = Solution().generateMatrix(matrix)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
