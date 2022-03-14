test_cases = int(input())

def insertion_sort_advanced_analysis(index_number_dictionary):
    count = 0
    largest_number = index_number_dictionary[0]
    for i in range(1, len(index_number_dictionary)):
        current_number_as_dict_value = index_number_dictionary[i]
        last_number_as_dict_value = index_number_dictionary[i - 1]

        if current_number_as_dict_value < largest_number:
            index_number_dictionary[i] = last_number_as_dict_value

            for j in range(i - 1, -1, -1):
                dict_value_being_compared_to = index_number_dictionary[j]
                if current_number_as_dict_value < dict_value_being_compared_to:
                    index_number_dictionary[j] = current_number_as_dict_value
                    index_number_dictionary[j+1] = dict_value_being_compared_to
                    count += 1

                else:
                    break

        else:

            largest_number = current_number_as_dict_value

    return count


for _ in range(test_cases):
    size = int(input())

    index_number_dictionary = {index: int(x) for index, x in enumerate(input().split())}

    print(insertion_sort_advanced_analysis(index_number_dictionary))

