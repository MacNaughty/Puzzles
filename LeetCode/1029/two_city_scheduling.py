import heapq
import unittest
from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[1] - x[0], reverse=True)

        n = len(costs) // 2
        total_cost = 0
        for i in range(n):
            total_cost += costs[i][0]
        for i in range(n, len(costs)):
            total_cost += costs[i][1]
        return total_cost


class MyTestCase(unittest.TestCase):

    def test_1(self):
        costs = [[10,20],[30,200],[400,50],[30,20]]
        actual = Solution().twoCitySchedCost(costs)
        expected = 110
        self.assertEqual(expected, actual)

    def test_2(self):
        costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
        actual = Solution().twoCitySchedCost(costs)
        expected = 1859
        self.assertEqual(expected, actual)

    def test_3(self):
        costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
        actual = Solution().twoCitySchedCost(costs)
        expected = 3086
        self.assertEqual(expected, actual)