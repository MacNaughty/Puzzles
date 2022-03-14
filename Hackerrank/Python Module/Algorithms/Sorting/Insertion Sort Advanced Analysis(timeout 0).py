test_cases = int(input())

def insertion_sort_1(key, key_index, result):
    count = 0

    # if the key is smaller than any of the result so far
    #   insert it add the beginning and update count the full length of result (that many swaps)
    if key < result[0]:
        count += len(result)
        result.insert(0, key)

    else:
        for j in range(len(result) - 1, -1, -1):
            if key >= result[j]:
                count += (key_index - (j + 1))
                result.insert(j + 1, key)
                break
    return count


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
