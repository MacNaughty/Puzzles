from collections import OrderedDict

test_cases = int(input())
print()

# since performing on the entire list causes the method to time out, we need to operate on a more abstract level
#   if it is not fast enough, we'll try OrderedDict
def collect_numbers_and_indices(full_list):

    # consecutive_and_first_occurrences is of the form: {number : last_consecutive_index}
    consecutive_and_first_occurrences = OrderedDict()
    consecutive_and_first_occurrences[full_list[0]] = 0
    last_element = full_list[0]

    for i in range(1, len(full_list)):

        # if the number, lst[i], is not already a key in the dictionary,
        #   add the number as the key, and the last occurring index in a row
        #   (we ignore the first set of consecutive elements to increase efficiency)
        #   for a large set of unique numbers, this might actually be slower
        if not full_list[i] in consecutive_and_first_occurrences.keys():
            consecutive_and_first_occurrences[full_list[i]] = i
            last_element = full_list[i]

        # if the lst[i] is already a key in the dictionary and is now occurring consecutively,
        #   increment its index (value) by 1
        #   otherwise ignore it
        elif full_list[i] == last_element:
            consecutive_and_first_occurrences[full_list[i]] += 1

    return consecutive_and_first_occurrences



def count_swaps(ordrd_dict, full_list):
    # if this approach doesn't work, then try building another dictionary in step one (with all values and indices)


    print(max(ordrd_dict.values()))
    count = 0
    # while some nonunique numbers are not in consecutive order (i.e. not sorted)
    #while(sum(ordrd_dict.values()) != len(full_list)):

        # if not, then we need to iterate through the elements after the largest value (index) in OrderedDict
        #   searching for the repetitive numbers


        #for i in range(max(ordrd_dict), len(full_list)):


    return count



for _ in range(test_cases):
    size = int(input())

    # set up array
    insertion_sort_analysis_full_list = list(map(int, input().split()))

    number_and_first_set_of_occurrences = collect_numbers_and_indices(insertion_sort_analysis_full_list)

    count = 0

    count += count_swaps(number_and_first_set_of_occurrences, insertion_sort_analysis_full_list)

