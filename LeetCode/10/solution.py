import unittest

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p_list = list(p)

        s_list = list(s)
        len_s = len(s)
        i = 0

        for j in range(len(p_list)):
            if p_list[j] == '.':
                i += 1
            elif p_list[j] == '*':
                prev_element = p_list[j-1]
                if prev_element == '.' or s_list[i] == prev_element:
                    k = j + 1
                    while k < len(p_list):
                        if self.isMatch(s[i:], p[k:]):
                            return True
                        k += 1

                    i += 1

            elif p_list[j] != s_list[i]:
                return False
            else:
                i += 1

        return i == len_s

class MyTestCase(unittest.TestCase):
    def test_1(self):
        s = "aa"
        p = "a"
        is_match = Solution().isMatch(s, p)
        self.assertEqual(is_match, False)

    def test_2(self):
        s = "aa"
        p = "a*"
        is_match = Solution().isMatch(s, p)
        self.assertEqual(is_match, True)

    def test_3(self):
        s = "aa"
        p = ".*"
        is_match = Solution().isMatch(s, p)
        self.assertEqual(is_match, True)  # add assertion here

    def test_4(self):
        s = "abcabd"
        p = "ab.*"
        is_match = Solution().isMatch(s, p)
        self.assertEqual(is_match, True)  # add assertion here

    def test_5(self):
        s = "aab"
        p = "c*a*b"
        is_match = Solution().isMatch(s, p)
        self.assertEqual(is_match, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()

    # if p_list[j] == '.':
    #     i += 1
    # elif p_list[j] == '*':
    #     # TODO:
    #     k = j - 2
    #     while k >= 0 and j < len(p_list) - 2:
    #         pattern = p_list[k:j - 1]
    #         s_substring = s[j:]
    #         k -= 1
