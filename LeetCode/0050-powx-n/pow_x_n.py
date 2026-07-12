import unittest
from collections import deque


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -n

        res = 1
        while n > 0:
            if n % 2 == 1:
                res *= x
            n = n // 2
            x *= x

        return res


class MyTestCase(unittest.TestCase):
    def test_0_1(self):
        x = 2
        n = 10
        expected = 1024
        actual = Solution().myPow(x, n)
        self.assertEqual(expected, actual)  # add assertion here

    def test_0(self):
        x = 2.1
        n = 3
        expected = 9.26100
        actual = Solution().myPow(x, n)
        self.assertEqual(expected, actual)  # add assertion here

    def test_1(self):
        x = 2.0
        n = -2
        expected = 0.25000
        actual = Solution().myPow(x, n)
        self.assertEqual(expected, actual)  # add assertion here

    def test_2(self):
        x = 0.00001
        n = 2147483647
        expected = 0.25000
        actual = Solution().myPow(x, n)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
