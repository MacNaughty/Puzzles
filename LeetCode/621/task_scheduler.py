import heapq
import unittest
from collections import defaultdict, Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        num_tasks = len(tasks)

        count_dict = Counter(tasks)

        tuple_list = sorted([[v, k] for k,v in count_dict.items()], reverse=True)
        task_cache = {}

        curr_interval = 0
        while num_tasks > 0:
            curr_interval += 1
            found_task = False
            for i in range(len(tuple_list)):
                task_tuple = tuple_list[i]
                task = task_tuple[1]
                if task in task_cache and task_cache[task] + n >= curr_interval:
                    continue

                found_task = True
                task_cache[task] = curr_interval

                if task_tuple[0] - 1 == 0:
                    tuple_list.pop(i)
                else:
                    task_tuple[0] -= 1
                num_tasks -= 1

                break

            if found_task:
                tuple_list.sort(reverse=True)

        return curr_interval

    def leastInterval(self, tasks, n):
        count_dict = Counter(tasks)

        # Create a max-heap based on task frequencies
        max_heap = [-v for v in count_dict.values()]
        heapq.heapify(max_heap)

        curr_interval = 0

        while max_heap:
            temp_list = []
            for i in range(n + 1):  # Process up to n+1 tasks to handle cooldown
                curr_interval += 1
                if max_heap:
                    freq = -heapq.heappop(max_heap)
                    if freq - 1 > 0:
                        temp_list.append(freq - 1)

                # All tasks are finished
                if not max_heap and not temp_list:
                    break

            # Add remaining tasks back to the heap
            for freq in temp_list:
                heapq.heappush(max_heap, -freq)

        return curr_interval

class MyTestCase(unittest.TestCase):
    def test_1(self):
        input = ["A","A","A","B","B","B"]
        expected = 8
        actual = Solution().leastInterval(input, 2)
        self.assertEqual(expected, actual)  # add assertion here

    def test_2(self):
        input = ["A","C","A","B","D","B"]
        expected = 6
        actual = Solution().leastInterval(input, 1)
        self.assertEqual(expected, actual)  # add assertion here

    def test_3(self):
        input = ["A","A","A", "B","B","B"]
        expected = 10
        actual = Solution().leastInterval(input, 3)
        self.assertEqual(expected, actual)  # add assertion here

    def test_4(self):
        input = ["B","B","B","C","D","E","F","G","H","I","J","K", "A","A","A"]
        expected = 20
        actual = Solution().leastInterval(input, 8)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
