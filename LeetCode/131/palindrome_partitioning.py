import unittest

def extend_partitions_with_palindromes(parts, end: int, dp: list[list[bool]]):
    out = set()

    for i in range(len(parts) - 1, -1, -1):
        start = parts[i][0]
        if dp[start][end]:
            out.add(parts[:i] + ((start, end),))

    return out

def is_palindrome_str(s: str) -> bool:
    for i in range(len(s) // 2):
        if s[i] != s[-(i+1)]:
            return False
    return True

def find_new_palindromes(tuple_str: tuple[str]) -> set[tuple[str]]:
    new_palindromes = set()
    for i in range(len(tuple_str) - 2, -1, -1):
        first: tuple[str] = tuple_str[:i]
        last: str = ''.join(tuple_str[i:])
        if is_palindrome_str(last):
            new_palindromes.add((*first, last) if first else (last,))

    return new_palindromes

def build_dp_array(s: str, n: int):
    dp = [[False] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            # length <= 3: middle section is automatically valid
            # e.g. "a", "aa", "aba"
            if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                dp[i][j] = True

    return dp

class Solution:

    def partition(self, s: str) -> list[list[str]]:
        n = len(s)
        dp = build_dp_array(s, n)

        res = []

        def dfs(start: int, path: list[str]):
            if start == n:
                res.append(path[:])
                return

            for end in range(start, n):
                if dp[start][end]:
                    dfs(end + 1, path + [s[start:end + 1]])

        dfs(0, [])
        return res

    def partition_v2(self, s: str) -> list[list[str]]:
        n = len(s)
        dp = build_dp_array(s, n)

        res = {((0, 0),)}

        for end in range(1, n):
            # append current character as its own piece
            res = {(*r, (end, end)) for r in res}

            new_parts = set()
            for r in res:
                new_parts |= extend_partitions_with_palindromes(r, end, dp)

            res |= new_parts

        return [[s[a:b+1] for a, b in r] for r in res]

    def partition_original(self, s: str) -> list[list[str]]:
        res: set[tuple[str]] = {(s[0],)}

        for i in range(1, len(s)):
            # 1. Append new char to existing lists
            new_res: set[tuple[str]] = set()
            for r in res:
                new_res.add((*r, s[i]))

            res = new_res

            # 2. check existing substr with addition of new char
            new_palindromes: set[tuple[str]] = set()
            for r in res:
                _new_palindromes = find_new_palindromes(r)
                for p in _new_palindromes:
                    new_palindromes.add(p)

            for p in new_palindromes:
                res.add(p)

        return [list(r) for r in res]

class MyTestCase(unittest.TestCase):
    def test_1(self):
        input = "aab"
        expected = [["a", "a", "b"], ["aa", "b"]]
        actual = Solution().partition(input)
        self.assertEqual(expected, actual)

    def test_2(self):
        input = "a"
        expected = [["a"]]
        actual = Solution().partition(input)
        self.assertEqual(expected, actual)

    def test_3(self):
        input = "fff"
        expected = [["f", "f", "f"], ["f", "ff"], ["ff", "f"], ["fff"]]
        actual = Solution().partition(input)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
