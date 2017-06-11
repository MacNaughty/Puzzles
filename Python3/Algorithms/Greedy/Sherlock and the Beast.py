from math import floor
from collections import Counter

number_of_testcases = int(input())

for _ in range(number_of_testcases):
    digits = int(input())
    result = -1


    # first we try numbers mod 3, this will eliminate the most possibilities
    #   because it is the highest possible value
    number_found = False
    if digits % 3 == 0:
        result = "5" * (3 * (digits // 3))
        number_found = True

    # make sure we haven't already found the result (if it was divisible by 3)
    if not number_found:

        # base base: check the four values that cannot cannot be factored by some combination of 3 and 5
        #   if digits is one of these values, skip the next step and print result as -1
        if (digits != 1) and (digits != 2) and (digits != 4) and (digits != 7):

            # we take the dividend of digits divided by 3, which will round down
            #   then we multiply by three to get as close as possible to digits while being less than digits
            number_of_fives = digits // 3
            number_of_fives *= 3

            # add clusters of three 5's until there are more 5's than digits
            while (number_of_fives < digits):
                number_of_fives += 3

            # we take away six "5"s and add five "3"s until the total of the two is equal to digits
            number_of_threes = 0
            while (number_of_fives + number_of_threes > digits):
                number_of_fives -= 6
                number_of_threes += 5

            result = ("5" * number_of_fives) + ("3" * number_of_threes)

    print(result)
