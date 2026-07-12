import unittest

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        res = [0] * (len(num1) + len(num2))

        for i in range(len(num1)-1, -1, -1):
            num1_digit = int(num1[i])
            carry = 0
            for j in range(len(num2)-1, -1, -1):
                num2_digit = int(num2[j])

                new_digit = (num1_digit * num2_digit) + carry + res[i+j+1]
                res[i+j+1] = new_digit % 10
                carry = new_digit // 10

            if carry:
                res[i] += carry

        # Convert result to string, strip leading zeros
        result_str = ''.join(map(str, res)).lstrip('0')
        return result_str if result_str else '0'








class MyTestCase(unittest.TestCase):
    def test_0(self):
        res = Solution().multiply("2", "0")
        self.assertEqual("0", res)  # add assertion here

    def test_1(self):
        res = Solution().multiply("2", "3")
        self.assertEqual("6", res)  # add assertion here

    def test_2(self):
        res = Solution().multiply("123", "456")
        self.assertEqual("56088", res)  # add assertion here


if __name__ == '__main__':
    unittest.main()
