import unittest
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        n = len(intervals)

        # Add all intervals that end before newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            i += 1
        start = i

        # Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        end = i

        return intervals[:start] + [newInterval] + intervals[end:]


class MyTestCase(unittest.TestCase):
    def test_1(self):
        intervals = [[1, 3], [6, 9]]
        newIntervals = [2, 5]
        expected = [[1, 5], [6, 9]]
        actual = Solution().insert(intervals, newIntervals)
        self.assertEqual(expected, actual)  # add assertion here

    def test_2(self):
        intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        newIntervals = [4, 8]
        expected = [[1, 2], [3, 10], [12, 16]]
        actual = Solution().insert(intervals, newIntervals)
        self.assertEqual(expected, actual)  # add assertion here

    def test_3(self):
        intervals = [[1, 2]]
        newIntervals = [3, 5]
        expected = [[1, 2], [3, 5]]
        actual = Solution().insert(intervals, newIntervals)
        self.assertEqual(expected, actual)  # add assertion here

    def test_4(self):
        intervals = [[1, 2], [6, 7], [8, 10], [12, 16]]
        newIntervals = [3, 5]
        expected = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        actual = Solution().insert(intervals, newIntervals)
        self.assertEqual(expected, actual)  # add assertion here

    def test_5(self):
        intervals = [[1, 2], [6, 7], [8, 10], [12, 16]]
        newIntervals = [3, 6]
        expected = [[1, 2], [3, 7], [8, 10], [12, 16]]
        actual = Solution().insert(intervals, newIntervals)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
