class Solution:
    def reverse1(self, x: int) -> int:
        if x == 0:
            return 0

        is_negative = True
        if x < 0:
            x *= -1
        else:
            is_negative = False

        max_32 = int("0x80000000", 16) if is_negative else int("0x7fffffff", 16)

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

    def reverse2(self, x: int) -> int:
        temp = str(abs(x))
        retval = int(temp[::-1])
        if (retval.bit_length() > 31):
            return 0
        if x < 0:
            return -1 * retval
        else:
            return retval
