import unittest
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def build_combinations(path: list, start):
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(start, n+1):
                path.append(i)
                build_combinations(path, i+1)
                path.pop()

        build_combinations([], 1)
        return res

class MyTestCase(unittest.TestCase):
    def test_1(self):
        n, k = 4, 2
        expected = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
        expected = [set(combo) for combo in expected]
        actual = Solution().combine(n, k)
        actual = [set(combo) for combo in actual]

        self.assertEqual(len(expected), len(actual))
        for combo in actual:
            self.assertIn(combo, expected)

    def test_2(self):
        n, k = 1, 1
        expected = [[1]]
        expected = [set(combo) for combo in expected]
        actual = Solution().combine(n, k)
        actual = [set(combo) for combo in actual]

        self.assertEqual(len(expected), len(actual))
        for combo in actual:
            self.assertIn(combo, expected)

if __name__ == '__main__':
    unittest.main()
