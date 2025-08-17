import unittest
from typing import List

from util.test_helper import MyTestCaseHelper


class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        last = n - 1

        for i in range(n // 2):
            for j in range(i, last-i):

                # counter-clockwise rotation
                # temp = matrix[i][j]
                # matrix[i][j] = matrix[j][last-i]
                # matrix[j][last-i] = matrix[last-i][last-j]
                # matrix[last-i][last-j] = matrix[last-j][i]
                # matrix[last-j][i] = temp

                temp = matrix[i][j]
                matrix[i][j] = matrix[last-j][i]
                matrix[last-j][i] = matrix[last-i][last-j]
                matrix[last-i][last-j] = matrix[j][last-i]
                matrix[j][last-i] = temp



class MyTestCase(unittest.TestCase):
    def test_1(self):
        input = [[1,2,3],[4,5,6],[7,8,9]]
        Solution().rotate(input)

        MyTestCaseHelper().assert_two_d_lists_equal([[7,4,1],[8,5,2],[9,6,3]], input)  # add assertion here

    def test_2(self):
        input = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        Solution().rotate(input)

        MyTestCaseHelper().assert_two_d_lists_equal([[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]], input)  # add assertion here


if __name__ == '__main__':
    unittest.main()
