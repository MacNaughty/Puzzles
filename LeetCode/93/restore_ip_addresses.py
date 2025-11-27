import unittest
from collections import defaultdict

from util.test_helper import MyTestCaseHelper

class Solution:
    def is_valid_part(self, substr: str):
        """Assumes: len(substr) <= 3"""


        if len(substr) > 1 and substr[0] == '0':
            return False

        return 0 <= int(substr) <= 255

    def restoreIpAddresses(self, s: str) -> list[str]:
        # this can be solved as subproblems, recursively
        if len(s) > 12:
            return []

        res = []

        first = defaultdict(list)
        for j in range(1, 4):
            if self.is_valid_part(s[:j]):
                first[j].append(s[:j])

        second = defaultdict(list)
        for i, first in first.items():
            for j in range(1, 4):
                if self.is_valid_part(s[i:i+j]):
                    second[i+j].append(first + [s[i:i + j]])

        third = defaultdict(list)
        for i, second_list in second.items():
            for j in range(1, 4):
                if self.is_valid_part(s[i:i+j]):
                    for elem in second_list:
                        third[i+j].append(elem + [s[i:i+j]])

        for i, third_list in third.items():
            for j in range(1, 4):
                if i + j == len(s) and self.is_valid_part(s[i:i + j]):
                    for elem in third_list:
                        res.append('.'.join(elem + [s[i:i + j]]))

        return res


class MyTestCase(MyTestCaseHelper):
    def test_1(self):
        input = "25525511135"
        expected = ["255.255.11.135", "255.255.111.35"]
        actual = Solution().restoreIpAddresses(input)
        self.assert_unordered_list_equal(expected, actual)

    def test_2(self):
        input = "0000"
        expected = ["0.0.0.0"]
        actual = Solution().restoreIpAddresses(input)
        self.assert_unordered_list_equal(expected, actual)

    def test_3(self):
        input = "101023"
        expected = ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
        actual = Solution().restoreIpAddresses(input)
        self.assert_unordered_list_equal(expected, actual)


if __name__ == '__main__':
    unittest.main()
