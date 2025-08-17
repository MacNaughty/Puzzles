import unittest
from collections import defaultdict
from heapq import heappop, heappush


# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY size
#  2. INTEGER_ARRAY cost
#

# def get_min(iterable):
#
#
#     return min_size

def getMinimalCost(size: list[int], cost: list[int])->int:
    # initialize global size dict
    size_dict = defaultdict(set)
    for i in range(len(size)):
        size_dict[size[i]].add(i)

    # initialize global duplicate dict
    dup_dict = defaultdict(set)
    for temp_size, indices in size_dict.items():
        if len(indices) > 1:
            dup_dict[temp_size].update(indices)


    total_cost = 0
    while len(dup_dict):
        min_size_dup = float('inf')
        for dup_size in dup_dict.keys():
            if dup_size < min_size_dup:
                min_size_dup = dup_size

        indices = dup_dict[min_size_dup]
        while len(indices) > 1:
            min_cost = float('inf')
            min_i = -1
            for i in indices:
                if cost[i] < min_cost:
                    min_cost = cost[i]
                    min_i = i

            size[min_i] += 1
            new_size = size[min_i]
            total_cost += cost[min_i]

            indices.remove(min_i)
            size_dict[new_size].add(min_i)
            size_dict[min_size_dup].remove(min_i)

            if len(size_dict[new_size]) > 1:
                dup_dict[new_size].update(size_dict[new_size])

            if len(dup_dict[min_size_dup]) == 1:
                del dup_dict[min_size_dup]

    return total_cost



from collections import defaultdict
from heapq import heappop, heappush

def getMinimalCost(size: list[int], cost: list[int]) -> int:
    size_dict = defaultdict(list)  # Maps size -> heap of (cost, index)
    min_dups_heap = []  # Min-heap to get the smallest duplicate size
    total_cost = 0

    # Populate size_dict
    for i in range(len(size)):
        heappush(size_dict[size[i]], (cost[i], i))

    # Populate min_heap with initial duplicate sizes
    for curr_size, indices in size_dict.items():
        if len(indices) > 1:
            heappush(min_dups_heap, curr_size)

    while min_dups_heap:
        min_size_dup = heappop(min_dups_heap)
        indices = size_dict[min_size_dup]

        while len(indices) > 1:  # Resolve duplicates
            min_cost, min_i = heappop(indices)  # Get lowest-cost duplicate
            size[min_i] += 1
            new_size = size[min_i]
            total_cost += min_cost

            heappush(size_dict[new_size], (cost[min_i], min_i))  # Move to new size

            if len(size_dict[new_size]) > 1:  # If new size has duplicates, add to heap
                heappush(min_dups_heap, new_size)

    return total_cost



class MyTestCase(unittest.TestCase):
    def test_1(self):
        input_size = [3, 7, 9, 7, 8]
        input_cost = [5, 2, 5, 7, 5]
        expected = 6
        actual = getMinimalCost(input_size, input_cost)


        self.assertEqual(expected, actual)  # add assertion here

    def test_2(self):
        input_size = [3, 3, 4, 5]
        input_cost = [5, 2, 2, 1]
        expected = 5
        actual = getMinimalCost(input_size, input_cost)

        self.assertEqual(expected, actual)

    def test_3(self):
        input_size = [1, 1, 1]
        input_cost = [1, 2, 3]
        expected = 4
        actual = getMinimalCost(input_size, input_cost)

        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()


list(map(int, "2 9 6 4 1 3 7 5 11 8 10".split()))
