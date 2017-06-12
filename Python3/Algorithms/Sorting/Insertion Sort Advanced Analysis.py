from array import array
# leaving this import because I tried swapping elements in arrays as well.
#   the code on this page is actually more effective for big swaps, but still times out

test_cases = int(input())


# refactored for starting index to be passed from second insertion_sort method
# and go until we reach the 0th element (down to, but not including, -1)
def insertion_sort_1(lst, starting_index, key_index):
    key = lst[key_index]
    count = 0
    if starting_index == 0:
        count += 1
        temp = lst[0]
        del lst[0]
        lst.insert(0, key)
        del lst[key_index]
        lst.insert(key_index, temp)

    else:
        for j in range(starting_index, -1, -1):
            if key >= lst[j]:
                count += (key_index - (j + 1))
                temp_j = lst[j + 1]
                del lst[j + 1]
                lst.insert(j, key)
                del lst[key_index]
                lst.insert(key_index - 1, temp_j)
                break
    return count



# using insertion_sort_1 with an unsorted, complete list
def insertion_sort_2(lst):
    count = 0
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            count += insertion_sort_1(lst, i - 1, i)
    print(count)

for _ in range(test_cases):
    size = int(input())

    # set up array
    insertion_sort_array_2 = list(map(int, input().split()))

    insertion_sort_2(insertion_sort_array_2)
