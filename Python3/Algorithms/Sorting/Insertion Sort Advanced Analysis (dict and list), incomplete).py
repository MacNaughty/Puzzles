from collections import OrderedDict
# leaving this import because I tried swapping elements in arrays as well.
#   the code on this page is actually more effective for big swaps, but still times out

test_cases = int(input())



def insertion_sort_1(number_to_be_added, numbers_index, result):
    count = int()
    if number_to_be_added < result[0]:
        count += len(result)
        result.insert(0, number_to_be_added)
        return count

    
    temp_dict = OrderedDict({k: v for v, k in enumerate(result)})
    # for values that are already contained in result
    if number_to_be_added in temp_dict:
        temp_dict[number_to_be_added] += 1
        result.insert(temp_dict[number_to_be_added], number_to_be_added)
        count = numbers_index - temp_dict[number_to_be_added]

    #else:
    
    return count

# using insertion_sort_1 with an unsorted, complete list
def insertion_sort_2(lst):
    count = 0
    result = []
    result.append(lst[0])
    for i in range(1, len(lst)):
        if lst[i] < result[i-1]:
            count += insertion_sort_1(lst[i], i, result)
        else:
            result.append(lst[i])
    print(count)

for _ in range(test_cases):
    size = int(input())

    # set up array
    insertion_sort_array_2 = list(map(int, input().split()))

    insertion_sort_2(insertion_sort_array_2)
