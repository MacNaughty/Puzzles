import unittest

def find_new_palindromes(parts, end, pal):
    out = set()

    for i in range(len(parts) - 1, -1, -1):
        start = parts[i][0]
        if pal[start][end]:
            out.add(parts[:i] + ((start, end),))

    return out

class Solution:

    def partition(self, s: str) -> list[list[str]]:
        n = len(s)
        pal = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                # length <= 3: middle section is automatically valid
                # e.g. "a", "aa", "aba"
                if s[i] == s[j] and (j - i <= 2 or pal[i + 1][j - 1]):
                    pal[i][j] = True

        res = {((0, 0),)}

        for end in range(1, n):
            # append current character as its own piece
            res = {(*r, (end, end)) for r in res}

            new_parts = set()
            for r in res:
                new_parts |= find_new_palindromes(r, end, pal)

            res |= new_parts

        return [[s[a:b+1] for a, b in r] for r in res]


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
