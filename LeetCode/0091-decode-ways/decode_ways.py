import unittest

class Solution:
    # def numDecodings(self, s: str) -> int:
    #     if s[0] == '0':
    #         return 0
    #
    #     for i in range(1, len(s)):
    #         if s[i] == '0' and s[i-1] == '0':
    #             return 0
    #
    #     res = 1
    #     for i in range(len(s)):
    #         if s[i] == '0':
    #             continue
    #         elif s[i] in {'1', '2'}:
    #             if i + 1 < len(s) and '0' < s[i+1] <= '6':
    #                 if not (i + 2 < len(s) and s[i+2] == '0'):
    #                     res += 1
    #
    #     return res

    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        for i in range(1, len(s)):
            if s[i] == '0' and s[i-1] not in {'1', '2'}:
                return 0

        prev2 = 1
        prev1 = 1
        for i in range(2, len(s)+1):
            curr = 0
            last_one = int(s[i-1])
            last_two = int(s[i-2:i])
            if 1 <= last_one <= 9:
                curr += prev1
            if 10 <= last_two <= 26:
                curr += prev2

            prev2, prev1 = prev1, curr

        return prev1


class MyTestCase(unittest.TestCase):

    def test_1(self):
        s = "12"
        expected = 2
        actual = Solution().numDecodings(s)
        self.assertEqual(expected, actual)

    def test_2(self):
        s = "226"
        expected = 3
        actual = Solution().numDecodings(s)
        self.assertEqual(expected, actual)

    def test_3(self):
        s = "06"
        expected = 0
        actual = Solution().numDecodings(s)
        self.assertEqual(expected, actual)

    def test_4(self):
        s = "10"
        expected = 1
        actual = Solution().numDecodings(s)
        self.assertEqual(expected, actual)

    def test_5(self):
        s = "1123"
        expected = 5
        actual = Solution().numDecodings(s)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
