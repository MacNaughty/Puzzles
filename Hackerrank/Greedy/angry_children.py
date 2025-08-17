import unittest
from collections import deque
def maxMin(k, arr):
    arr.sort()
    n = len(arr)

    res = float('inf')
    for i in range(n-k+1):
        window_max = arr[i+k-1]
        window_min = arr[i]
        res = min(res, window_max - window_min)

    return res



class MyTestCase(unittest.TestCase):
    def test_1(self):
        k = 2
        arr = [1, 4, 7, 2]
        expected = 1
        actual = maxMin(k, arr)
        self.assertEqual(expected, actual)

    def test_2(self):
        k = 3
        arr = [10, 100, 300, 200, 1000, 20, 30]
        expected = 20
        actual = maxMin(k, arr)
        self.assertEqual(expected, actual)

    def test_3(self):
        k = 5
        arr = [4504, 1520, 5857, 4094, 4157, 3902, 822, 6643, 2422, 7288, 8245, 9948, 2822, 1784, 7802, 3142, 9739, 5629, 5413, 7232]
        expected = 1335
        actual = maxMin(k, arr)
        self.assertEqual(expected, actual)

    def test_4(self):
        k = 3
        arr = [100, 200, 300, 350, 400, 401, 402]
        expected = 2
        actual = maxMin(k, arr)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
