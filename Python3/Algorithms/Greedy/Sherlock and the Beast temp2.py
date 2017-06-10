def helper_function_starting_with_threes(list_of_threes):
    temp_length = len(list_of_threes)
    for i in range(temp_length - 5, -1, -5):
        if ((temp_length - i + 5) % 5 == 0) and (temp_length - i + 5) % 3 == 0:
            list_of_threes = list_of_threes.replace("3" * i, "5" * i)
            break
    return list_of_threes


def helper_function_starting_with_fives(list_of_mostly_fives):
    temp_length = len(list_of_mostly_fives)
    for i in range(temp_length, -1, -3):
        if ((temp_length - i) % 3 == 0) and (temp_length - i) % 5 == 0:
            list_of_mostly_fives = list_of_mostly_fives.replace("3" * i, "5" * i)
    return list_of_mostly_fives



for ...
multiples_of_three = reversed([x*3 for x in range(1, ceil(digits / 3))])
        multiples_of_five = [y*5 for y in range(1, ceil(digits / 5))]
        for quintuple in multiples_of_five:
            if result != -1:
                if len(result) == digits:
                    break
            for triple in multiples_of_three:
                if digits % (triple + quintuple) == 0:
                    multiplier = digits // (triple + quintuple)
                    result = ("5" * triple * multiplier) + ("3" * quintuple * multiplier)
                    break



            # termination argument - otherwise the list will continue expanding
