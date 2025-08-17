import unittest
from collections import deque


# class Solution:
    # def minDistance(self, word1: str, word2: str) -> int:
    #     """
    #     convert word1 into word2
    #     return (min) num operations
    #     3 operations
    #         Insert a character
    #         Delete a character
    #         Replace a character
    #     """
    #     len1 = len(word1)
    #     len2 = len(word2)
    #     if len1 == 0:
    #         return len2
    #     if len2 == 0:
    #         return len1
    #
    #     dp = [[0] * (len2+1) for _ in range(len1+1)]
    #     for i in range(len1+1):
    #         dp[i][0] = i
    #     for j in range(len2+1):
    #         dp[0][j] = j
    #
    #     for i in range(1, len1+1):
    #         for j in range(1, len2+1):
    #             if word1[i-1] == word2[j-1]:
    #                 dp[i][j] = dp[i-1][j-1]
    #             else:
    #                 dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
    #
    #     return dp[-1][-1]

    # def minDistance(self, word1: str, word2: str) -> int:
    #     """
    #     convert word1 into word2
    #     return (min) num operations
    #     3 operations
    #         Insert a character
    #         Delete a character
    #         Replace a character
    #     """
    #     len1 = len(word1)
    #     len2 = len(word2)
    #     if len1 == 0:
    #         return len2
    #     if len2 == 0:
    #         return len1
    #
    #     dp = [0] * (len2+1)
    #     # for i in range(len1+1):
    #     #     dp[i][0] = i
    #     for j in range(len2+1):
    #         dp[j] = j
    #
    #     for i in range(1, len1+1):
    #         for j in range(1, len2+1):
    #             if word1[i-1] == word2[j-1]:
    #                 dp[j] = dp[j-1]
    #             else:
    #                 dp[j] = 1 + min(dp[j-1], dp[j])
    #
    #     return dp[-1]

    # def minDistance(self, word1: str, word2: str) -> int:
    #     """
    #     convert word1 into word2
    #     return (min) num operations
    #     3 operations
    #         Insert a character
    #         Delete a character
    #         Replace a character
    #     """
    #     len1 = len(word1)
    #     len2 = len(word2)
    #     if len1 == 0:
    #         return len2
    #     if len2 == 0:
    #         return len1
    #     prev = list(range(len2 + 1))  # dp[0][j] = j
    #
    #     for i in range(1, len1 + 1):
    #         curr = [0] * (len2 + 1)
    #         curr[0] = i  # dp[i][0] = i
    #
    #         for j in range(1, len2 + 1):
    #             if word1[i-1] == word2[j-1]:
    #                 curr[j] = prev[j-1]  # No change needed
    #             else:
    #                 curr[j] = 1 + min(prev[j],   # Delete
    #                               curr[j-1],  # Insert
    #                               prev[j-1])  # Replace
    #
    #         prev = curr  # Move current row to previous row
    #
    #     return prev[len2]

def minDistance(self, word1: str, word2: str) -> int:
    q = deque()

    q.append((0,0))
    w1 = len(word1)
    w2 = len(word2)
    dist = 0
    visit = set()

    while(q):
        for _ in range(len(q)):
            i,j = q.popleft()

            while i < w1 and j < w2 and word1[i] == word2[j]:
                i += 1
                j += 1

            if i == w1 and j == w2:
                return dist

            for (newi, newj) in [(i+1,j),(i,j+1),(i+1,j+1)]:
                if newi <= w1 and newj <= w2 and (newi,newj) not in visit:
                    visit.add((newi,newj))
                    q.append((newi,newj))

        dist += 1
class MyTestCase(unittest.TestCase):
    def test_1(self):
        word1 = "horse"
        word2 = "ros"
        expected = 3
        actual = Solution().minDistance(word1, word2)
        self.assertEqual(expected, actual)

    def test_2(self):
        word1 = "intention"
        word2 = "execution"
        expected = 5
        actual = Solution().minDistance(word1, word2)
        self.assertEqual(expected, actual)

    def test_3(self):
        word1 = "abcdef"
        word2 = "abef"
        expected = 2
        actual = Solution().minDistance(word1, word2)
        self.assertEqual(expected, actual)

    def test_4(self):
        word1 = "distance"
        word2 = "springbok"
        expected = 9
        actual = Solution().minDistance(word1, word2)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
