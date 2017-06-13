from collections import OrderedDict

test_cases = int(input())
print()

# since performing on the entire list causes the method to time out, we need to operate on a more abstract level
#   if it is not fast enough, we'll try OrderedDict
def collect_numbers_and_indices(full_list):

    count = 0


    # elements_and_first_occurrence is of the form: {number : last_consecutive_index}
    elements_and_first_occurrence = OrderedDict()
    elements_and_first_occurrence[full_list[0]] = 0
    last_element = full_list[0]

    index_increment = dict()


    for i in range(1, len(full_list)):
        number_being_placed = full_list[i]


        # if the number, lst[i], is not already a key in the dictionary,
        #   add the number as the key, and the last consecutive index as the value
        #   (we ignore the first set of consecutive elements to increase efficiency)
        #   (e.g. [1, 1, 1, 3, 2] becomes {1 : 2, 3 : 3, 2 : 4}
        #       for a large set of unique numbers, this might actually be slower
        if not number_being_placed in elements_and_first_occurrence:
            elements_and_first_occurrence[number_being_placed] = i
            last_element = number_being_placed


        # if lst[i] is already a key in the dictionary and is now occurring consecutively,
        #   increment its index (value) by 1
        elif number_being_placed == last_element:
            elements_and_first_occurrence[number_being_placed] += 1

        # if lst[i] IS already a key in the main dictionary and is NOT occurring consecutively,
        #else:
            # add it to the dict and add corresponding increment value




    return elements_and_first_occurrence




for _ in range(test_cases):
    size = int(input())

    # set up array
    insertion_sort_analysis_full_dict = [int(i) for i in input().split()]

    print(collect_numbers_and_indices(insertion_sort_analysis_full_dict))

    count = 0

    #count += count_swaps(numbers_and_indices)
