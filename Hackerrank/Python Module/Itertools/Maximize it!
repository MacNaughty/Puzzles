k_m = list(map(int, input().split()))
K = k_m[0]
M = k_m[1]
list_of_all_combinations = []

# List(x1, x2, x3,...) -> List(x1**2, x2**2, x3**2,...)
def all_squares(Ni):
    temp_result = []
    for number in Ni:
        temp_result.append(number**2)
    return temp_result

# all_combinations_so_far -> new_list_of_all_combinations
def build_all_combinations(list_of_squares):

    # we're going to build every possible combination so far using new list of squares
    # with the a copied version of the global variable list_of_all_combinations
    # and duplicate the old list of combinations
    new_list_of_all_combinations = []
    length_for_iterations = len(list_of_all_combinations)
    for square in list_of_squares:

        # duplicate the original list_of_all_combinations
        cloned_list_of_all_combinations = []
        for i in range(length_for_iterations):
            cloned_list_of_all_combinations.append(list(list_of_all_combinations[i]))

        # append each square onto the end of each nested list in the clone
        for i in range(length_for_iterations):
            cloned_list_of_all_combinations[i].append(square)

        # append each combination onto the end of the new list of combinations
        for combination in cloned_list_of_all_combinations:
            new_list_of_all_combinations.append(combination)

    # clear the global variable list_of_all_combinations and replace it with new_list...
    del list_of_all_combinations[:]
    for i in range(len(new_list_of_all_combinations)):
        list_of_all_combinations.append(new_list_of_all_combinations[i])

# setup for equation (assigning global
list_of_list_of_all_squares = []
for i in range(K):
    Ni_input_line = list(map(int, input().split()))

    list_of_list_of_all_squares.append(all_squares(sorted(Ni_input_line[1:])))
    # now each list is mapped to a new list where f(x) is applied (all_squares),
    # nested lists of all squares are all contained within list_of_list_of_all_squares
    #   must check in ascending order: check every possible combination (modulo makes this necessary


def final_function(nested_lists_of_squares):
    result = -1
        
    # trivial case: K = 1
    # we assume that all nested squares has only one list of squares
    # take the highest single result after mod M
    if K == 1:
        for list_of_squares in nested_lists_of_squares[0]:
            if list_of_squares % M > result:
                result = list_of_squares % M


    # base case: list_of_lists_of_combinations_so_far is empty
    #   thus we fill it with single element lists from list_of_squares
    for list_of_squares in nested_lists_of_squares[0]:
        list_of_all_combinations.append([list_of_squares])


    # for the rest: build all combinations of elements
    for list_of_squares in nested_lists_of_squares[1:]:
        build_all_combinations(list_of_squares)


    # compare all combinations to find the highest result (mod M)
    for combination in list_of_all_combinations:
        if sum(combination) % M > result:
            result = sum(combination) % M

    print(result)

final_function(list_of_list_of_all_squares)
