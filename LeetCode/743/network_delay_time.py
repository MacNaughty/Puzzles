import heapq
import unittest
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # Min-heap: (distance from k, node)
        heap = [(0, k)]
        visited = set()

        max_weight = 0

        while heap:
            weight, u = heapq.heappop(heap)
            if u in visited:
                continue

            visited.add(u)
            max_weight = max(max_weight, weight)

            for v, w in graph[u]:
                if v not in visited:
                    heapq.heappush(heap, (weight+w, v))

        return max_weight if len(visited) == n else -1

class MyTestCase(unittest.TestCase):
    def test_1(self):
        times = [[2,1,1],[2,3,1],[3,4,1]]
        n = 4
        k = 2

        expected = 2
        actual = Solution().networkDelayTime(times, n, k)
        self.assertEqual(expected, actual)

    def test_2(self):
        times = [[1,2,1]]
        n = 2
        k = 1

        expected = 1
        actual = Solution().networkDelayTime(times, n, k)
        self.assertEqual(expected, actual)

    def test_3(self):
        times = [[1,2,1]]
        n = 2
        k = 2

        expected = -1
        actual = Solution().networkDelayTime(times, n, k)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
