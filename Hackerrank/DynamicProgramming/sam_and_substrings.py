import unittest

# MOD = 10**9 + 7
# def substrings(n):
#     res = 0
#     for i in range(len(n)):
#         if MOD - int(n[i]) <= res:
#             res = (MOD - res) + int(n[i])
#         else:
#             res += int(n[i]) % MOD
#         for j in range(i+1, len(n)):
#             if MOD - int(n[i:j+1]) <= res:
#                 res = (res + int(n[i:j+1])) % MOD
#             else:
#                 res += int(n[i:j+1])
#
#     return res

MOD = 10**9 + 7
def substrings(n):
    res = 0
    p = 1

    for i in range(len(n) - 1, -1, -1):
        if MOD - res <= int(n[i]) * (i + 1) * p:
            res = (int(n[i]) * (i + 1) * p) - (MOD - res)
        else:
            res += int(n[i]) * (i + 1) * p
        if MOD // 10 <= p + 1:
            p = MOD - p + 1
        else:
            p = (p * 10 + 1) % MOD

    return res

class MyTestCase(unittest.TestCase):
    def test_1(self):
        n = "16"
        expected = 23
        actual = substrings(n)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
