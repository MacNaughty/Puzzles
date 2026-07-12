import unittest


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True

        digit_char_list = list(str(x))
        num_digits = len(digit_char_list)

        for i in range(num_digits):
            if i > num_digits - 1 - i:
                return True
            elif digit_char_list[i] != digit_char_list[num_digits - 1 - i]:
                return False

class MyTestCase(unittest.TestCase):
    def test_1(self):
        x = 121
        is_palidrome = Solution().isPalindrome(x)
        self.assertEqual(True, is_palidrome)  # add assertion here

    def test_2(self):
        x = -121
        is_palidrome = Solution().isPalindrome(x)
        self.assertEqual(False, is_palidrome)  # add assertion here

    def test_3(self):
        x = 10
        is_palidrome = Solution().isPalindrome(x)
        self.assertEqual(False, is_palidrome)  # add assertion here

    def test_4(self):
        x = 14441
        is_palidrome = Solution().isPalindrome(x)
        self.assertEqual(True, is_palidrome)  # add assertion here

    def test_5(self):
        x = 1
        is_palidrome = Solution().isPalindrome(x)
        self.assertEqual(True, is_palidrome)  # add assertion here


if __name__ == '__main__':
    unittest.main()
