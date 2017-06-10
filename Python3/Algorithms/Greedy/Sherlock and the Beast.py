number_of_testcases = int(input())

for _ in range(number_of_testcases):
    digits = int(input())

    result = -1

    # iterate through combinations of numbers mod 3 and numbers mod 5
    #   starting with numbers mod 5, because numbers mod 3 must be in inner nested loop
    #       (this is because numbers mod 3 will create a larger number
    #       as was described in the problem statement)

    # i represents multiples of 3, and clusters of "555"
    i = 3
    while digits >= i:
        # j represents multiples of 5, and clusters of "33333"
        j = 0
        while digits >= i + j:
            if digits % (i + j) == 0:
                result = ""
                multiplier = digits // (i + j)
                result += "5" * (i * multiplier)
                result += "3" * (j * multiplier)
            j += 5
        i += 3



    print(result)


