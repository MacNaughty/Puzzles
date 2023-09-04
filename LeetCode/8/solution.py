import unittest

class Solution:

    MAX_INT     = 0x7FFFFFFF
    MIN_INT_POS = 0x80000000

    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0

        is_negative = False
        i = 0
        if s[0] == '-':
            is_negative = True
            i += 1
        elif s[0] == '+':
            i += 1

        if i == len(s) or not s[i].isdigit():
            return 0

        j = i
        while j < len(s) and s[j].isdigit():
            j += 1

        result = int(s[i:j])
        if is_negative and result > self.MIN_INT_POS:
            return -self.MIN_INT_POS
        elif not is_negative and result > self.MAX_INT:
            return self.MAX_INT

        return -result if is_negative else result

class MyTestCase(unittest.TestCase):
    def test_1(self):
        s = "42"
        res = Solution().myAtoi(s)

        self.assertEqual(res, 42)

    def test_2(self):
        s = "   -42"
        res = Solution().myAtoi(s)

        self.assertEqual(res, -42)

    def test_3(self):
        s = "4193 with words"
        res = Solution().myAtoi(s)

        self.assertEqual(res, 4193)

    def test_4(self):
        s = "words and 987"
        res = Solution().myAtoi(s)

        self.assertEqual(res, 0)

    def test_5(self):
        s = "00000-42a1234"
        res = Solution().myAtoi(s)

        self.assertEqual(res, 0)


if __name__ == '__main__':
    unittest.main()
