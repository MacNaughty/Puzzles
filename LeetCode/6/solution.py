import unittest


class Solution(object):

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        len_s = len(s)
        if numRows == 1 or len_s <= numRows:
            return s

        s_list = list(s)

        zig_vertical_index_set = {0, numRows - 1}
        factor = 2 * (numRows - 1)

        res = [None]*len_s
        i = 0

        row_num = 0
        while row_num < numRows:
            col_num = 0

            while (col_num * factor) + row_num < len_s:
                res[i] = s_list[(col_num * factor) + row_num]
                i += 1

                if row_num not in zig_vertical_index_set and ((col_num+1) * factor) - row_num < len_s:
                    res[i] = s_list[((col_num+1) * factor) - row_num]
                    i += 1

                col_num += 1

            row_num += 1

        return ''.join(res)


class MyTestCase(unittest.TestCase):
    def test_1(self):
        s = "PAYPALISHIRING"
        numRows = 3
        res = Solution().convert(s, numRows)

        self.assertEqual(res, "PAHNAPLSIIGYIR")

    def test_2(self):
        s = "PAYPALISHIRING"
        numRows = 4
        res = Solution().convert(s, numRows)

        self.assertEqual(res, "PINALSIGYAHRPI")

    def test_3(self):
        s = "A"
        numRows = 1
        res = Solution().convert(s, numRows)

        self.assertEqual(res, "A")  # add assertion here


if __name__ == '__main__':
    unittest.main()
