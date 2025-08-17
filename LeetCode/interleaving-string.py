import unittest

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            k = i + j

            if k == len(s3):
                return i == len(s1) and j == len(s2)

            # try to take from first side
            if i < len(s1) and s1[i] == s3[k]:
                if dfs(i+1, j):
                    memo[(i, j)] = True
                    return True

            if j < len(s2) and s2[j] == s3[k]:
                if dfs(i, j+1):
                    memo[(i, j)] = True
                    return True

            memo[(i, j)] = False
            return False

        return dfs(0, 0)

class MyTestCase(unittest.TestCase):
    def test_1(self):
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbcbcac"
        expected = True
        actual = Solution().isInterleave(s1, s2, s3)
        self.assertEqual(expected, actual)

    def test_2(self):
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbbaccc"
        expected = False
        actual = Solution().isInterleave(s1, s2, s3)
        self.assertEqual(expected, actual)

    def test_3(self):
        s1 = ""
        s2 = ""
        s3 = ""
        expected = True
        actual = Solution().isInterleave(s1, s2, s3)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
