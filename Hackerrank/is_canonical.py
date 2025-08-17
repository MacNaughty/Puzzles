import math
import unittest


def is_canonical(denominations):
    def greedy(n):
        """Greedy algorithm to minimize coins for amount n."""
        count = 0
        for coin in reversed(denominations):
            count += n // coin
            n %= coin
        return count

    def dp(n):
        """DP algorithm to minimize coins for amount n."""
        # Initialize DP array with infinity for all values
        dp_arr = [float('inf')] * (n + 1)
        dp_arr[0] = 0

        for i in range(1, n + 1):
            for coin in denominations:
                if i >= coin:
                    dp_arr[i] = min(dp_arr[i], dp_arr[i - coin] + 1)
        return dp_arr[n]

    # Calculate the LCM of the two largest denominations
    lcm_limit = math.lcm(denominations[-1], denominations[-2])

    # Check for all amounts up to the LCM of the largest denominations
    for n in range(1, lcm_limit + 1):
        if greedy(n) != dp(n):
            return f"❌ Not Canonical! Greedy fails for amount {n}. Greedy: {greedy(n)}, DP: {dp(n)}"

    return "✅ Canonical System! Greedy works for all amounts."

# Example systems to test
canonical_system = [1, 3, 4, 6]
non_canonical_system_1 = [1, 3, 4, 5]
non_canonical_system_2 = [1, 4, 6]

print(is_canonical(canonical_system))         # ✅ Should be canonical
print(is_canonical(non_canonical_system_1))   # ❌ Should not be canonical
print(is_canonical(non_canonical_system_2))   # ❌ Should not be canonical


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
