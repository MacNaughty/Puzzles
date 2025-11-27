import unittest

from util.test_helper import MyTestCaseHelper


class Solution:
    def grayCode(self, n: int) -> list[int]:
        total = 1 << n
        path: list[int] = [0]
        visited = {0}  # Use a set of integers for O(1) lookups

        # O(1) check for differing by one bit
        def is_gray_next(num1, num2):
            diff = num1 ^ num2
            return diff > 0 and (diff & (diff - 1) == 0)

        def backtrack():
            if len(path) == total:
                # Gray Code path found! The final check (last vs first) is not needed for
                # this problem, as any valid path is accepted.
                return True

            current_num = path[-1]

            # Generate the only n potential next candidates in O(n)
            for j in range(n):
                flip_mask = 1 << j
                candidate = current_num ^ flip_mask  # Flip the j-th bit

                if candidate not in visited:
                    path.append(candidate)
                    visited.add(candidate)

                    if backtrack():
                        return True

                    # Backtrack (undo the choice)
                    visited.remove(candidate)
                    path.pop()

            return False

        backtrack()
        return path



class MyTestCase(MyTestCaseHelper):
    def test_1(self):
        input = 2
        expected = [[0,1,3,2], [0,2,3,1]]
        actual = Solution().grayCode(input)
        self.assert_list_is_one_of(expected, actual)

    def test_2(self):
        input = 3
        expected = [[0,1,3,2,6,7,5,4]]
        actual = Solution().grayCode(input)
        self.assert_list_is_one_of(expected, actual)

    def test_3(self):
        input = 4
        expected = [[0,1,3,2,6,7,5,4]]
        actual = Solution().grayCode(input)
        self.assert_list_is_one_of(expected, actual)


if __name__ == '__main__':
    unittest.main()
