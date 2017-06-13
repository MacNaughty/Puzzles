from array import array
# leaving this import because I tried swapping elements in arrays as well.
#   the code on this page is actually more effective for big swaps, but still times out

test_cases = int(input())



def insertion_sort_1(lst, key_index, result):
    key = lst[key_index]
    count = 0

    # if the key is smaller than any of the result so far
    #   insert it add the beginning and update count the full length of result (that many swaps)
    if key < result[0]:
        count += len(result)
        result.insert(0, key)

    else:
        for j in range(1, len(result)):
            if key < result[j]:
                count += (key_index - (j))
                result.insert(j, key)
                break
    return count



# using insertion_sort_1 with an unsorted, complete list
def insertion_sort_2(lst):
    count = 0
    result = []
    result.append(lst[0])
    for i in range(1, len(lst)):
        if lst[i] < result[i-1]:
            count += insertion_sort_1(lst, i, result)
        else:
            result.append(lst[i])
    print(count)

for _ in range(test_cases):
    size = int(input())

    # set up array
    insertion_sort_array_2 = list(map(int, input().split()))

    insertion_sort_2(insertion_sort_array_2)
