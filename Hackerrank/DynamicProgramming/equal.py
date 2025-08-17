import unittest

# def equal(arr):
#     def min_operations(x):
#         operations = 0
#         for num in arr:
#             diff = num - x
#             operations += diff // 5 + (diff % 5) // 2 + (diff % 5 % 2)
#         return operations
#
#     # Try minimizing to min(arr), min(arr) - 1, min(arr) - 2 (handles edge cases)
#     min_val = min(arr)
#     return min(min_operations(min_val - i) for i in range(3))

def equal(arr):
    min_val = min(arr)
    result = float('inf')

    # Try minimizing to min_val, min_val - 1, ..., min_val - 4
    for target in range(min_val, min_val - 5, -1):
        total_operations = 0
        for num in arr:
            diff = num - target
            total_operations = diff // 5 + (diff % 5) // 2 + (diff % 5) % 2

        result = min(result, total_operations)

    return result



class MyTestCase(unittest.TestCase):
    def test_1(self):
        arr = [2, 2, 3, 7]
        expected = 2
        actual = equal(arr)
        self.assertEqual(expected, actual)

    def test_2(self):
        arr = [10, 7, 12]
        expected = 3
        actual = equal(arr)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
