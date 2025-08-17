import unittest

def cost(B: list[int]) -> int:
    lenB = len(B)
    if lenB == 1:
        return 0  # Only one element means no differences to sum.

    low = 0  # Max sum if A[i] = 1 at previous step
    high = 0  # Max sum if A[i] = B[i] at previous step

    for i in range(1, lenB):
        prev_high = B[i - 1]  # Previous element in B
        curr_high = B[i]  # Current element in B

        # If we set A[i] = 1, then we consider:
        # - A[i-1] was either 1 (low) or B[i-1] (high)
        high_to_1 = high + abs(prev_high - 1)  # Transition from A[i-1] = B[i-1] to A[i] = 1

        # If we set A[i] = B[i], then we consider:
        # - A[i-1] was either 1 (low) or B[i-1] (high)
        low_to_curr_high = low + abs(curr_high - 1)  # Transition from A[i-1] = 1 to A[i] = B[i]
        high_to_curr_high = high + abs(curr_high - prev_high)  # Transition from A[i-1] = B[i-1] to A[i] = B[i]

        # Compute new possible values
        low_new = max(low, high_to_1)  # Max sum if A[i] = 1
        high_new = max(low_to_curr_high, high_to_curr_high)  # Max sum if A[i] = B[i]

        # Update low and high for the next iteration
        low, high = low_new, high_new

    return max(low, high)  # Return the maximum sum possible


class MyTestCase(unittest.TestCase):
    def test_1(self):
        B = [1, 2, 3]
        expected = 2
        actual = cost(B)
        self.assertEqual(expected, actual)

    def test_2(self):
        B = [10, 1, 10, 1, 10]
        expected = 36
        actual = cost(B)
        self.assertEqual(expected, actual)

    def test_3(self):
        B = [100, 2, 100, 2, 100]
        expected = 396
        actual = cost(B)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
