import unittest
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_balance = 0
        curr_balance = 0
        start_index_res = 0

        for i in range(n):
            balance = gas[i] - cost[i]
            total_balance += balance
            curr_balance += balance
            if curr_balance < 0:
                curr_balance = 0
                start_index_res = i + 1

        return -1 if total_balance < 0 else start_index_res


class MyTestCase(unittest.TestCase):
    def test_1(self):
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]
        expected = 3
        actual = Solution().canCompleteCircuit(gas, cost)
        self.assertEqual(expected, actual)

    def test_2(self):
        gas = [2, 3, 4]
        cost = [3, 4, 3]
        expected = -1
        actual = Solution().canCompleteCircuit(gas, cost)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
