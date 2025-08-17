import unittest
# Complete the getMinimumCost function below.
import heapq
from functools import reduce


def getMinimumCost(k, c):
    c.sort(reverse=True)
    total_cost = 0

    for i in range(len(c)):
        total_cost += (i // k + 1) * c[i]

    return total_cost


class MyTestCase(unittest.TestCase):
    def test_1(self):
        c = [1, 2, 3, 4]
        k = 3
        expected = 11
        actual = getMinimumCost(k, c)
        self.assertEqual(expected, actual)

    def test_2(self):
        c = [1, 3, 5, 7, 9]
        k = 3
        expected = 29
        actual = getMinimumCost(k, c)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
