import unittest
from bisect import bisect_right
from typing import List


class Solution:
    # def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    #
    #     res = []
    #     for i in range(len(profit)):
    #         curr_start = startTime[i]
    #         curr_end = endTime[i]
    #         curr_profit = profit[i]
    #
    #         has_conflict = False
    #         for j, (prev_start, prev_end, prev_profit) in enumerate(res):
    #             if curr_start < prev_end:
    #                 has_conflict = True
    #                 break
    #
    #         if not has_conflict:
    #             res.append((curr_start, curr_end, curr_profit))
    #         else:
    #             conflict_indices = set()
    #             for j, (prev_start, prev_end, prev_profit) in enumerate(res):
    #                 if curr_start < prev_end:
    #                     conflict_indices.add(j)
    #
    #             existing_profit = 0
    #             for j in conflict_indices:
    #                 existing_profit += res[j][2]
    #
    #             if existing_profit < curr_profit:
    #                 for j in conflict_indices:
    #                     res[j] = (float('inf'), float('-inf'), 0)
    #                 res.append((curr_start, curr_end, curr_profit))
    #
    #     total_profit = 0
    #     for curr_start, curr_end, curr_profit in res:
    #         total_profit += curr_profit
    #
    #     return total_profit

    # def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    #     potential_schedule_list: list[list[tuple[int, int, int]]] = []
    #     for i in range(len(startTime)):
    #         curr_start = startTime[i]
    #         curr_end = endTime[i]
    #         curr_profit = profit[i]
    #
    #         potential_schedule_list.append([(curr_start, curr_end, curr_profit)])
    #
    #
    #     for i in range(len(startTime)):
    #         curr_start = startTime[i]
    #         curr_end = endTime[i]
    #         curr_profit = profit[i]
    #
    #         compatible_schedule_list = []
    #         for schedule in potential_schedule_list:
    #             is_compatible = True
    #             for (prev_start, prev_end, prev_profit) in schedule:
    #                 if curr_start < prev_end and curr_end > prev_start:
    #                     is_compatible = False
    #                     break
    #
    #             if is_compatible:
    #                 new_schedule = [(prev_start, prev_end, prev_profit) for (prev_start, prev_end, prev_profit) in schedule]
    #                 new_schedule.append((curr_start, curr_end, curr_profit))
    #                 compatible_schedule_list.append(new_schedule)
    #
    #
    #         for schedule in compatible_schedule_list:
    #             potential_schedule_list.append(schedule)
    #
    #     max_profit = 0
    #     for schedule in potential_schedule_list:
    #         schedule_profit = 0
    #         for (curr_start, curr_end, curr_profit) in schedule:
    #             schedule_profit += curr_profit
    #
    #         if schedule_profit > max_profit:
    #             max_profit = schedule_profit
    #
    #     return max_profit

    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        # Combine job data and sort by end time
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        startTime, endTime, profit = zip(*jobs)

        num_jobs = len(profit)

        dp = [0]*(num_jobs+1)

        for i in range(1, num_jobs+1):
            curr_start, curr_end, curr_profit = startTime[i-1], endTime[i-1], profit[i-1]

            idx = bisect_right(endTime, curr_start, 0, i-1)

            dp[i] = max(dp[i-1], dp[idx] + curr_profit)

        return dp[num_jobs]


class MyTestCase(unittest.TestCase):
    def test_1(self):
        startTime = [1,2,3,3]
        endTime = [3,4,5,6]
        profit = [50,10,40,70]

        expected = 120
        actual = Solution().jobScheduling(startTime, endTime, profit)

        self.assertEqual(expected, actual)  # add assertion here

    def test_2(self):
        startTime = [1,2,3,4,6]
        endTime = [3,5,10,6,9]
        profit = [20,20,100,70,60]

        expected = 150
        actual = Solution().jobScheduling(startTime, endTime, profit)

        self.assertEqual(expected, actual)  # add assertion here

    def test_3(self):
        startTime = [6,15,7,11,1,3,16,2]
        endTime = [19,18,19,16,10,8,19,8]
        profit = [2,9,1,19,5,7,3,19]

        expected = 41
        actual = Solution().jobScheduling(startTime, endTime, profit)

        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
