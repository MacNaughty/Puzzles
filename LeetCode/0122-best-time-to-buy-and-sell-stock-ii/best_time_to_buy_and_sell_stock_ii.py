import unittest
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        total_profit = 0
        for day in range(len(prices)-1):
            if prices[day] < prices[day+1]:
                total_profit += prices[day+1] - prices[day]

        return total_profit

    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        if n == 0:
            return 0

        # Initialize DP arrays
        dp = [[0] * 2 for _ in range(n)]

        # Base cases
        dp[0][0] = 0  # No stock on day 0
        dp[0][1] = -prices[0]  # Bought on day 0

        # Fill DP table
        for i in range(1, n):
            # No stock today: Max of not buying or selling today
            best_profit_without_stock = dp[i-1][0]
            best_profit_with_stock = dp[i-1][1]
            dp[i][0] = max(best_profit_without_stock, best_profit_with_stock + prices[i])
            # Own stock today: Max of holding or buying today
            dp[i][1] = max(best_profit_with_stock, best_profit_without_stock - prices[i])

        # Max profit at the end with no stock in hand
        return dp[n-1][0]



class MyTestCase(unittest.TestCase):
    def test_1(self):
        prices = [7,1,5,3,6,4]
        expected = 7
        actual = Solution().maxProfit(prices)
        self.assertEqual(expected, actual)

    def test_2(self):
        prices = [1,2,3,4,5]
        expected = 4
        actual = Solution().maxProfit(prices)
        self.assertEqual(expected, actual)

    def test_3(self):
        prices = [7,6,4,3,1]
        expected = 0
        actual = Solution().maxProfit(prices)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
