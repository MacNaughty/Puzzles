from collections import Counter
from math import ceil

number_of_testcases = int(input())

for _ in range(number_of_testcases):
    digits = int(input())
    result = -1
    found = False

    # base case: digits = 5 (only case that can't be handled by the algorithm
    if digits == 5:
        result = "33333"
        found = True

    # first check for divisibility mod 3, since that eliminates the most possibilities
    if digits % 3 == 0:
        result = "5" * digits
        found = True

    if not found:
        # for numbers larger than the sum of the two (other than 5, which has already been checked)
        if digits >= 5 + 3:

            # take a multiple of 3 that is minimally larger than digits
            total_5s = ceil(digits / 3) * 3

            total_3s = 0
            # reduce groups of "555" + "555" (length 6), and replace them with "33333" (length 5)
            #   until the sum of the two is equal to digits
            while (total_3s + total_5s > digits):
                total_5s -= 6
                total_3s += 5

            # build the result
            result = ("5" * total_5s) + ("3" * total_3s)

    print(result)
