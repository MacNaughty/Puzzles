import unittest
from collections import deque


class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = deque()

        for part in path.split('/'):
            if part == '..':
                if parts:
                    parts.pop()
            elif part not in {'', '.'}:
                parts.append(part)

        return '/' + '/'.join(parts)


class MyTestCase(unittest.TestCase):
    def test_0_1(self):
        input = "/"
        expected = "/"
        actual = Solution().simplifyPath(input)
        self.assertEqual(expected, actual)  # add assertion here

    def test_0(self):
        input = "home"
        expected = "/home"
        actual = Solution().simplifyPath(input)
        self.assertEqual(expected, actual)  # add assertion here

    def test_1(self):
        input = "/home/"
        expected = "/home"
        actual = Solution().simplifyPath(input)
        self.assertEqual(expected, actual)  # add assertion here

    def test_2(self):
        input = "/home//foo/"
        expected = "/home/foo"
        actual = Solution().simplifyPath(input)
        self.assertEqual(expected, actual)  # add assertion here

    def test_3(self):
        input = "/home/user/Documents/../Pictures"
        expected = "/home/user/Pictures"
        actual = Solution().simplifyPath(input)
        self.assertEqual(expected, actual)  # add assertion here

    def test_4(self):
        input = "/../"
        expected = "/"
        actual = Solution().simplifyPath(input)
        self.assertEqual(expected, actual)  # add assertion here

    def test_5(self):
        input = "/.../a/../b/c/../d/./"
        expected = "/.../b/d"
        actual = Solution().simplifyPath(input)
        self.assertEqual(expected, actual)  # add assertion here

    def test_6(self):
        input = "/a/../../b/../c//.//"
        expected = "/c"
        actual = Solution().simplifyPath(input)
        self.assertEqual(expected, actual)  # add assertion here


if __name__ == '__main__':
    unittest.main()
