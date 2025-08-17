import unittest
from collections import Counter
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m = len(board)
        n = len(board[0])

        # Early pruning
        if Counter(word) - Counter(c for row in board for c in row):
            return False

        def dfs(i, j, word_index):
            if board[i][j] != word[word_index]:
                return False
            if word_index == len(word) - 1:
                return True

            # Mark visited
            temp = board[i][j]
            board[i][j] = '#'

            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != '#':
                    if dfs(ni, nj, word_index + 1):
                        return True

            # Restore original value
            board[i][j] = temp
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False


class MyTestCase(unittest.TestCase):
    def test_1(self):
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "ABCCED"
        expected = True
        actual = Solution().exist(board, word)
        self.assertEqual(expected, actual)

    def test_2(self):
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "SEE"
        expected = True
        actual = Solution().exist(board, word)
        self.assertEqual(expected, actual)

    def test_3(self):
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
        word = "ABCB"
        expected = False
        actual = Solution().exist(board, word)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
