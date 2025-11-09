import unittest

from util.test_helper import MyTestCaseHelper


class Solution:
    def grayCode(self, n: int) -> list[int]:
        total = 1 << n  # 2^n
        path = [0]
        visited = [False] * total
        visited[0] = True
        memo = set()  # to remember failed (node, visited_mask) states

        def backtrack(node, visited_mask):
            # base case: all nodes used
            if len(path) == total:
                return True

            # memoization: skip failed subproblems
            if (node, visited_mask) in memo:
                return False

            # try flipping each bit (moving along 1-bit edges)
            for bit in range(n):
                next_node = node ^ (1 << bit)  # flip one bit
                if not visited[next_node]:
                    visited[next_node] = True
                    path.append(next_node)

                    if backtrack(next_node, visited_mask | (1 << next_node)):
                        return True

                    # backtrack
                    visited[next_node] = False
                    path.pop()

            # mark this state as failed
            memo.add((node, visited_mask))
            return False

        backtrack(0, 1)
        return path


class MyTestCase(MyTestCaseHelper):
    def test_1(self):
        input = 2
        expected = [[0,1,3,2], [0,2,3,1]]
        actual = Solution().grayCode(input)
        self.assert_list_is_one_of(expected, actual)

    # def test_2(self):
    #     input = 4
    #     expected = [[]]
    #     actual = Solution().grayCode(input)
    #     self.assert_list_is_one_of(expected, actual)


if __name__ == '__main__':
    unittest.main()
