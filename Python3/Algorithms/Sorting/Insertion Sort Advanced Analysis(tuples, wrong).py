from collections import OrderedDict

test_cases = int(input())


for _ in range(test_cases):
    size = int(input())

    count = 0

    # set up array
    full_tuples = tuple((int(value)) for value in (input().split()))
    full_tuples_unsorted = (tuple((int(value), index) for index, value in enumerate(full_tuples)))
    full_dict_unsorted = OrderedDict()
    for tpl in full_tuples_unsorted:
        full_dict_unsorted[tpl] = 0

    full_tuples_sorted = tuple(sorted(full_tuples_unsorted))

    for i in range(len(full_tuples)):
        sorted_tuple = full_tuples_sorted[i]
        for j in range(i + 1, full_tuples_unsorted.index(sorted_tuple) + 1):
            unsorted_tuple = full_tuples_unsorted[j]
            if sorted_tuple != unsorted_tuple:
                full_dict_unsorted[unsorted_tuple] += 1
            else:
                count += abs(i - j + full_dict_unsorted[unsorted_tuple])

    print(count)
