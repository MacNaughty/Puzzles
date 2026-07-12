import unittest
from functools import lru_cache


class Solution:

    # def isMatch(self, s: str, p: str) -> bool:
    #     cache = [[False] * (len(p) + 1) for i in range(len(s) + 1)]
    #     cache[len(s)][len(p)] = True
    #
    #     for s_i in range(len(s), -1, -1):
    #         for p_i in range(len(p) - 1, -1, -1):
    #             match = s_i < len(s) and p[p_i] in {s[s_i], "."} # Matching current character
    #
    #             if (p_i + 1) < len(p) and p[p_i + 1] == "*": # Handling * (Zero or More of Preceding Character)
    #                 cache[s_i][p_i] = cache[s_i][p_i + 2] # Ignore "*"
    #                 if match:
    #                     cache[s_i][p_i] = cache[s_i][p_i] or cache[s_i + 1][p_i] # Use "*" (consume s[i])
    #             elif match:
    #                 cache[s_i][p_i] = cache[s_i + 1][p_i + 1] # Handling Simple Character Match (. or Exact Match)
    #
    #     return cache[0][0]

    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if j >= len(p):
                return i >= len(s)

            match = i < len(s) and (p[j] in {s[i], "."})
            if (j + 1) < len(p) and p[j + 1] == "*":
                cache[(i, j)] = dfs(i, j + 2) or (  # dont use *
                        match and dfs(i + 1, j)
                )  # use *
                return cache[(i, j)]
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            cache[(i, j)] = False
            return False

        return dfs(0, 0)

    # def isMatch(self, s: str, p: str) -> bool:
    #     @lru_cache(None)  # Memoization to store previously computed results
    #     def dp(s_i: int, p_i: int) -> bool:
    #         if p_i == len(p):  # Pattern is exhausted
    #             return s_i == len(s)  # String must also be exhausted
    #
    #         first_match = s_i < len(s) and (p[p_i] == s[s_i] or p[p_i] == '.')
    #
    #         if p_i + 1 < len(p) and p[p_i + 1] == '*':  # Handle '*' case
    #             return dp(s_i, p_i + 2) or (first_match and dp(s_i + 1, p_i))
    #
    #         return first_match and dp(s_i + 1, p_i + 1)
    #
    #     return dp(0, 0)


    # def isMatch(self, s: str, p: str) -> bool:
    #     @lru_cache(None)  # Memoization to store previously computed results
    #     def dp(s, p):
    #         s_i = 0
    #         p_i = 0
    #         while p_i < len(p) and s_i < len(s):
    #             curr_p = p[p_i]
    #             curr_s = s[s_i]
    #             if curr_p not in {'*', '.'}:
    #                 if curr_p == curr_s:
    #                     if len(p) > p_i + 1 and p[p_i + 1] == '*':
    #                         s_i_0 = s_i
    #                         while s_i_0 < len(s) and s[s_i_0] == p[p_i]:
    #                             if dp(s[s_i_0:], p[p_i+2:]):
    #                                 return True
    #                             s_i_0 += 1
    #
    #                     s_i += 1
    #                     p_i += 1
    #                 else: # curr_p != curr_s
    #                     if p_i < len(p) - 2 and p[p_i+1] == '*':
    #                         # s_i += 1
    #                         p_i += 2
    #                     else:
    #                         return False
    #             else:
    #                 if curr_p == '.':
    #                     if p_i+1 == len(p):
    #                         return s_i == len(s) - 1
    #                     next_p = p[p_i+1]
    #                     if next_p == '*':
    #                         if p_i+2 == len(p):
    #                             return True
    #
    #                         for j in range(s_i, len(s)):
    #                             if dp(s[j:], p[p_i+2:]):
    #                                 return True
    #
    #                         return False
    #
    #                     else:
    #                         s_i += 1
    #                         p_i += 1
    #                 else:
    #                     if p_i+1 == len(p):
    #                         return s_i == len(s) - 1
    #                     if dp(s[s_i:], p[p_i-1:]) or \
    #                             (p_i < len(p) - 1 and dp(s[s_i:], p[p_i+1:])):
    #                         return True
    #
    #                     p_i += 1
    #                     if p[p_i-1] == curr_s:
    #                         s_i += 1
    #
    #         if p_i == len(p) and s_i == len(s):
    #             return True
    #         elif p_i in {len(p)-1, len(p)-2}:
    #             if p_i == len(p)-1 and p[p_i] == '*':
    #                 return True
    #             elif p_i == len(p)-2 and p[p_i+1] in {'*', s[s_i-1]}:
    #                 return s_i >= len(s)
    #             else:
    #                 return False
    #         else:
    #             return False
    #
    #     return dp(s, p)

    # def isMatch(self, s: str, p: str) -> bool:
    #
    #
    #     memoization = {}
    #     def dp(s: str, p: str):
    #         if f'{s}:{p}' in memoization:
    #             return memoization[f'{s}:{p}']
    #
    #         s_i = 0
    #         p_i = 0
    #         while p_i < len(p) and s_i < len(s):
    #             curr_p = p[p_i]
    #             curr_s = s[s_i]
    #             if curr_p not in {'*', '.'}:
    #                 if curr_p == curr_s:
    #                     if len(p) > p_i + 1 and p[p_i + 1] == '*':
    #                         s_i_0 = s_i
    #                         while s_i_0 < len(s) and s[s_i_0] == p[p_i]:
    #                             if f'{s_i_0}:{p_i+2}' in memoization:
    #                                 return memoization[f'{s_i_0}:{p_i+2}']
    #                             if dp(s[s_i_0:], p[p_i+2:]):
    #                                 memoization[f'{s_i_0}:{p_i+2}'] = True
    #                                 return True
    #                             s_i_0 += 1
    #
    #                     s_i += 1
    #                     p_i += 1
    #                 else: # curr_p != curr_s
    #                     if p_i < len(p) - 2 and p[p_i+1] == '*':
    #                         # s_i += 1
    #                         p_i += 2
    #                     else:
    #                         memoization[f'{s}:{p}'] = False
    #                         return False
    #             else:
    #                 if curr_p == '.':
    #                     if p_i+1 == len(p):
    #                         memoization[f'{s}:{p}'] = s_i == len(s) - 1
    #                         return s_i == len(s) - 1
    #                     next_p = p[p_i+1]
    #                     if next_p == '*':
    #                         if p_i+2 == len(p):
    #                             memoization[f'{s}:{p}'] = True
    #                             return True
    #
    #                         for j in range(s_i, len(s)):
    #                             if f'{s}:{p_i+2}' in memoization:
    #                                 return memoization[f'{s}:{p_i+2}']
    #                             if dp(s[j:], p[p_i+2:]):
    #                                 memoization[f'{s}:{p_i+2}'] = True
    #                                 return True
    #
    #                         memoization[f'{s}:{p}'] = False
    #                         return False
    #
    #                     else:
    #                         s_i += 1
    #                         p_i += 1
    #                 else:
    #                     if p_i+1 == len(p):
    #                         memoization[f'{s}:{p}'] = s_i == len(s) - 1
    #                         return s_i == len(s) - 1
    #
    #                     if f'{s[s_i:]}:{p[p_i - 1:]}' in memoization:
    #                         return memoization[f'{s[s_i:]}:{p[p_i - 1:]}']
    #                     if p_i < len(p) - 1 and f'{s[s_i:]}:{p[p_i+1:]}' in memoization:
    #                         return memoization[f'{s[s_i:]}:{p[p_i+1:]}']
    #                     if dp(s[s_i:], p[p_i-1:]) or (p_i < len(p) - 1 and dp(s[s_i:], p[p_i+1:])):
    #                         memoization[f'{s[s_i:]}:{p[p_i+1:]}'] = True
    #                         return True
    #
    #                     p_i += 1
    #                     if p[p_i-1] == curr_s:
    #                         s_i += 1
    #
    #         if p_i == len(p) and s_i == len(s):
    #             memoization[f'{s}:{p}'] = True
    #             return True
    #         elif p_i in {len(p)-1, len(p)-2}:
    #             if p_i == len(p)-1 and p[p_i] == '*':
    #                 memoization[f'{s}:{p}'] = True
    #                 return True
    #             elif p_i == len(p)-2 and p[p_i+1] in {'*', s[s_i-1]}:
    #                 memoization[f'{s}:{p}'] = s_i >= len(s)
    #                 return s_i >= len(s)
    #             else:
    #                 memoization[f'{s}:{p}'] = False
    #                 return False
    #         else:
    #             memoization[f'{s}:{p}'] = False
    #             return False
    #
    #     memoization[f'{s}:{p}'] = dp(s, p)
    #     return memoization[f'{s}:{p}']


class MyTestCase(unittest.TestCase):
    def test_neg1(self):
        s = "a"
        p = "ab*a"
        is_match = Solution().isMatch(s, p)
        self.assertEqual(is_match, False)


    def test_0(self):
        s = "a"
        p = "ab*"
        is_match = Solution().isMatch(s, p)
        self.assertEqual(is_match, True)

    def test_1(self):
        s = "aa"
        p = "a"
        is_match = Solution().isMatch(s, p)
        self.assertEqual(is_match, False)

    def test_2(self):
        s = "aa"
        p = "a*"
        is_match = Solution().isMatch(s, p)
        self.assertEqual(is_match, True)

    def test_3(self):
        s = "aa"
        p = ".*"
        is_match = Solution().isMatch(s, p)
        self.assertEqual(is_match, True)  # add assertion here

    def test_4(self):
        s = "abcabd"
        p = "ab.*"
        is_match = Solution().isMatch(s, p)
        self.assertEqual(is_match, True)  # add assertion here

    def test_5(self):
        s = "aab"
        p = "c*a*b"
        is_match = Solution().isMatch(s, p)
        self.assertEqual(is_match, True)  # add assertion here

    def test_6(self):
        s = "aaa"
        p = "a*a"
        is_match = Solution().isMatch(s, p)
        self.assertEqual(is_match, True)  # add assertion here

    def test_8(self):
        s = "aaa"
        p = "ab*a"
        is_match = Solution().isMatch(s, p)
        self.assertEqual(False, is_match)  # add assertion here

    def test_9_1(self):
        s = 'issippi'
        p = 'is*p*.'
        is_match = Solution().isMatch(s, p)
        self.assertEqual(False, is_match)  # add assertion here

    def test_9(self):
        s = "mississippi"
        p = "mis*is*p*."
        is_match = Solution().isMatch(s, p)
        self.assertEqual(is_match, False)  # add assertion here

    def test_10(self):
        s = "aaa"
        p = "ab*a*c*a"
        is_match = Solution().isMatch(s, p)
        self.assertEqual(is_match, True)  # add assertion here

    def test_11(self):
        s = "bbbba"
        p = ".*a*a"
        is_match = Solution().isMatch(s, p)
        self.assertEqual(is_match, True)  # add assertion here

    def test_12(self):
        s = "abbbcd"
        p = "ab*bbbcd"
        is_match = Solution().isMatch(s, p)
        self.assertEqual(is_match, True)  # add assertion here

    def test_13(self):
        s = "aaaaaaaaaaaaab"
        p = "a*a*a*a*a*a*a*a*a*c"
        is_match = Solution().isMatch(s, p)
        self.assertEqual(is_match, False)  # add assertion here

    def test_14(self):
        s = "bb"
        p = ".bab"
        is_match = Solution().isMatch(s, p)
        self.assertEqual(is_match, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()

    # if p_list[j] == '.':
    #     i += 1
    # elif p_list[j] == '*':
    #     # TODO:
    #     k = j - 2
    #     while k >= 0 and j < len(p_list) - 2:
    #         pattern = p_list[k:j - 1]
    #         s_substring = s[j:]
    #         k -= 1
