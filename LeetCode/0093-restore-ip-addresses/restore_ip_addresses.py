import unittest
from collections import defaultdict

from util.test_helper import MyTestCaseHelper

class Solution:

    def restoreIpAddresses(self, s: str) -> list[str]:
        len_s = len(s)
        if not 4 <= len_s <= 12:
            return []

        def is_valid_part(substr: str) -> bool:
            """
            Checks if a string slice is a valid IP segment.
              - must not have leading zeros unless it is the single digit '0'
              - must be between 0 and 255
            ASSUMES: len(substr) <= 3 (due to loop range)
            """
            if len(substr) > 1 and substr[0] == '0':
                return False

            return 0 <= int(substr) <= 255

        def get_next_stage_parts(current_parts, max_remaining_len):
            next_parts = defaultdict(list)

            for i, partial_addresses in current_parts.items():
                for j in range(1, 4):

                    new_i = i + j
                    remaining_len = len_s - new_i
                    if not 0 <= remaining_len <= max_remaining_len:
                        continue

                    substr = s[i:new_i]
                    if is_valid_part(substr):
                        for part_list in partial_addresses:
                            next_parts[new_i].append(part_list + [substr])

            return next_parts

        parts = {0: [[]]}
        for i in [9, 6, 3, 0]:
            parts = get_next_stage_parts(parts, i)

        return ['.'.join(part) for part in parts[len_s]]


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

    def test_4(self):
        input = "1111"
        expected = ["1.1.1.1"]
        actual = Solution().restoreIpAddresses(input)
        self.assert_unordered_list_equal(expected, actual)


if __name__ == '__main__':
    unittest.main()
