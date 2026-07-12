import unittest
from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegrees = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegrees[course] += 1

        q = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)

        res = []
        while q:
            course = q.popleft()
            res.append(course)
            for prereq in graph[course]:
                indegrees[prereq] -= 1
                if indegrees[prereq] == 0:
                    q.append(prereq)

        return res if len(res) == numCourses else []


class MyTestCase(unittest.TestCase):
    def test_1(self):
        numCourses = 2
        prerequisites = [[1, 0]]
        expected = [0, 1]

        actual = Solution().findOrder(numCourses, prerequisites)
        self.assertEqual(expected, actual)  # add assertion here

    def test_2(self):
        numCourses = 4
        prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
        expected = [0, 2, 1, 3]

        actual = Solution().findOrder(numCourses, prerequisites)
        self.assertEqual(expected, actual)  # add assertion here

    def test_3(self):
        numCourses = 1
        prerequisites = []
        expected = [0]

        actual = Solution().findOrder(numCourses, prerequisites)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
