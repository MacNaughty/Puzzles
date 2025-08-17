import unittest
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top, left = 0, 0
        bottom, right = n - 1, n - 1
        curr = 1
        res = [[1]*n for _ in range(n)]
        while top <= bottom and left <= right:
            for i in range(left, right+1):
                res[top][i] = curr
                curr += 1
            top += 1

            for i in range(top, bottom+1):
                res[i][right] = curr
                curr += 1
            right -= 1

            for i in range(right, left-1, -1):
                res[bottom][i] = curr
                curr += 1
            bottom -= 1

            for i in range(bottom, top-1, -1):
                res[i][left] = curr
                curr += 1
            left += 1
        return res



class MyTestCase(unittest.TestCase):
    def test_1(self):
        n = 3
        expected = [[1,2,3],[8,9,4],[7,6,5]]
        actual = Solution().generateMatrix(n)
        self.assertEqual(expected, actual)
    #
    # def test_2(self):
    #     n = 3
    #     expected = [[1,2,3],[8,9,4],[7,6,5]]
    #     actual = Solution().generateMatrix(n)
    #     self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
