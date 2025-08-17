import unittest

# def abbreviation(a, b):
#     if len(a) < len(b):
#         return "NO"
#
#     def has_rem_upper(i):
#         for k in range(i, len(a)):
#             if 'A' <= a[k] <= 'Z':
#                 return False
#         return True
#
#     i = 0
#     j = 0
#     streak_length = 0
#     while i < len(a) and j < len(b):
#         if len(a) - i + streak_length < len(b): return "NO"
#         if len(b) == streak_length:
#             if has_rem_upper(i):
#                 streak_length = 0
#                 continue
#             else:
#                 return "YES"
#
#         if b[j] in {a[i], a[i].upper()}:
#             streak_length += 1
#             i += 1
#             j += 1
#
#         elif 'a' <= a[i] <= 'z':
#             i += 1
#
#         else:
#             streak_length = 0
#             i += 1
#
#
#     return "YES" if len(b) == streak_length and not has_rem_upper(i) else "NO"

def abbreviation(a, b):
    n, m = len(a), len(b)

    # Create DP table with False as default values
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    # Empty a can become empty b
    dp[0][0] = True

    # Fill the first row - handle case where only lowercase letters are deleted
    for i in range(1, n + 1):
        if a[i - 1].islower():
            dp[i][0] = dp[i - 1][0]
        else:
            dp[i][0] = False

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1].upper() == b[j - 1]:  # If it matches after converting to uppercase
                dp[i][j] = dp[i - 1][j - 1]
            if a[i - 1].islower():  # Option to ignore lowercase letters
                dp[i][j] = dp[i][j] or dp[i - 1][j]


    # Final answer is whether we can form the entire b from a
    return "YES" if dp[n][m] else "NO"



class MyTestCase(unittest.TestCase):

    def test_0(self):
        a = "daBcd"
        b = "ABC"
        expected = "YES"
        actual = abbreviation(a, b)
        self.assertEqual(expected, actual)

    def test_1(self):
        a = "AbcDE"
        b = "ABDE"
        expected = "YES"
        actual = abbreviation(a, b)
        self.assertEqual(expected, actual)  # add assertion here

    def test_2(self):
        input = [
            ("Pi", "P"),
            ("AfPZN", "APZNC"),
            ("LDJAN", "LJJM"),
            ("UMKFW", "UMKFW"),
            ("KXzQ", "K"),
            ("LIT", "LIT"),
            ("QYCH", "QYCH"),
            ("DFIQG", "DFIQG"),
            ("sYOCa", "YOCN"),
            ("JHMWY", "HUVPW"),
        ]

        expected_outputs = [
            "YES",
            "NO",
            "NO",
            "YES",
            "NO",
            "YES",
            "YES",
            "YES",
            "NO",
            "NO",
        ]
        for i, (a, b) in enumerate(input):
            expected = expected_outputs[i]
            actual = abbreviation(a, b)
            self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
