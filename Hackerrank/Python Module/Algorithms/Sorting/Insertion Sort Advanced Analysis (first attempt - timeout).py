test_cases = int(input())

def insertion_sort_advanced_analysis(number_list):
    count = 0
    for i in range(1, len(number_list)):

        if number_list[i] < number_list[i - 1]:
            current_number = number_list[i]
            number_list[i] = number_list[i-1]
            number_list[i-1] = current_number
            count += 1

            j = i - 2
            while(current_number < number_list[j] and j >= 0):
                number_list[j+1] = number_list[j]
                number_list[j] = current_number
                count += 1
                j -= 1

    return count

for _ in range(test_cases):
    size = int(input())

    index_number_dictionary = [int(x) for x in input().split()]

    print(insertion_sort_advanced_analysis(index_number_dictionary))
