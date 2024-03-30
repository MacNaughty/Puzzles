import unittest
from typing import List


class Solution:

    def maxArea(self, height: List[int]) -> int:
        n = len(height)

        max_area = 0
        i = 0
        j = n - 1

        def find_next_i(curr_i):
            k = curr_i + 1
            while k < j and height[curr_i] >= height[k]:
                k += 1

            return k if k < j else None

        def find_next_j(curr_j):
            k = curr_j - 1
            while i < k and height[curr_j] >= height[k]:
                k -= 1

            return k if i < k else None

        while i < j:
            min_height = min(height[i], height[j])
            max_area = max(max_area, min_height * (j-i))

            if height[i] < height[j]:
                i = find_next_i(i)
            elif height[i] > height[j]:
                j = find_next_j(j)
            else:
                i = find_next_i(i)
                if i is None:
                    break
                j = find_next_j(j)

            if i is None or j is None:
                break

        return max_area


class MyTestCase(unittest.TestCase):
    def test_1(self):
        height = [1,8,6,2,5,4,8,3,7]
        self.assertEqual(49, Solution().maxArea(height))  # add assertion here

    def test_2(self):
        height = [1,1]
        self.assertEqual(1, Solution().maxArea(height))  # add assertion here


if __name__ == '__main__':
    unittest.main()
