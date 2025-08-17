import unittest
from typing import List


class Solution:
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     if amount == 0:
    #         return 0
    #     if amount in coins:
    #         return 1
    #     if amount in {c*2 for c in coins}:
    #         return 2
    #
    #     # TODO: if coins is canonical, use greedy
    #     coins.sort()
    #     largest_coin = coins[-1]
    #     remaining_amount = amount % largest_coin
    #     num_coins = amount // largest_coin
    #     if remaining_amount == 0:
    #         return num_coins
    #
    #     remaining_amount += 2 * largest_coin
    #     num_coins -= 2
    #
    #     res = float('inf')
    #     for i in range(len(coins)-1, -1, -1):
    #         mod_in_subset = remaining_amount
    #         num_coins_in_subset = num_coins
    #
    #         for j in range(i, -1, -1):
    #             while mod_in_subset >= coins[j]:
    #                 mod_in_subset -= coins[j]
    #                 num_coins_in_subset += 1
    #
    #         if mod_in_subset == 0:
    #             res = min(res, num_coins_in_subset)
    #
    #     return -1 if res == float('inf') else res


# class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], 1 + dp[i-coin])

        return -1 if dp[-1] == float('inf') else dp[-1]


class MyTestCase(unittest.TestCase):
    def test_1(self):
        coins = [1,2,5]
        amount = 11
        expected = 3
        actual = Solution().coinChange(coins, amount)
        self.assertEqual(expected, actual)

    def test_2(self):
        coins = [2]
        amount = 3
        expected = -1
        actual = Solution().coinChange(coins, amount)
        self.assertEqual(expected, actual)

    def test_3(self):
        coins = [1]
        amount = 0
        expected = 0
        actual = Solution().coinChange(coins, amount)
        self.assertEqual(expected, actual)

    def test_4(self):
        coins = [1, 3, 5]
        amount = 4
        expected = 2
        actual = Solution().coinChange(coins, amount)
        self.assertEqual(expected, actual)

    def test_5(self):
        coins = [1,2147483647]
        amount = 2
        expected = 2
        actual = Solution().coinChange(coins, amount)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
