class Solution:
    def reverse1(self, x: int) -> int:
        if x == 0:
            return 0

        if x < 0:
            x *= -1
            is_negative = True
        else:
            is_negative = False

        max_32 = 0x80000000 if is_negative else 0x7fffffff

        result = 0
        while x > 0:
            next_digit = x % 10
            next_result = (result * 10) + next_digit
            if next_result > max_32:
                return 0
            else:
                result = (result * 10) + next_digit
                x //= 10

        if is_negative:
            return result*-1
        else:
            return result
