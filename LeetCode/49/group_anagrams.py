import unittest
from collections import defaultdict
from typing import List


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            res[''.join(sorted(s))].append(s)
        return list(res.values())


class MyTestCase(unittest.TestCase):
    def test_1(self):
        actual = Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
        for element in actual:
            element_set = set(element)
            self.assertIn(element_set, [{"bat"},{"nat","tan"},{"ate","eat","tea"}])

    def test_2(self):
        actual = Solution().groupAnagrams(["hhhhu","tttti","tttit","hhhuh","hhuhh","tittt"])

        for element in actual:
            element_set = set(element)
            self.assertIn(element_set, [{"tittt","tttit","tttti"},{"hhhhu","hhhuh","hhuhh"}])


if __name__ == '__main__':
    unittest.main()
