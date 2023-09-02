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

        factor = 2 * (numRows - 1)

        res = [None]*len_s
        i = 0

        row_num = 0
        while row_num < numRows:
            col_num = 0

            while row_num + col_num * factor < len_s:
                res[i] = s_list[row_num + (col_num * factor)]
                i += 1

                if row_num not in {0, numRows - 1} and (factor * (col_num+1)) - row_num < len_s:
                    res[i] = s_list[(factor * (col_num+1)) - row_num]
                    i += 1

                col_num += 1

            row_num += 1

        return ''.join(res)

    # # def convert(self, s, numRows):
    #     """
    #     :type s: str
    #     :type numRows: int
    #     :rtype: str
    #     """
    #
    #     len_s = len(s)
    #     if numRows == 1 or len_s <= numRows:
    #         return s
    #
    #     s_list = list(s)
    #
    #     factor = 2 * (numRows - 1)
    #
    #     res = ''
    #
    #     row_num = 0
    #     while row_num < numRows:
    #         col_num = 0
    #
    #         while row_num + col_num * factor < len_s:
    #             res = f'{res}{s_list[row_num + (col_num * factor)]}'
    #             if row_num not in {0, numRows - 1} and (factor * (col_num + 1)) - row_num < len_s:
    #                 res = f'{res}{s_list[(factor * (col_num + 1)) - row_num]}'
    #             col_num += 1
    #         row_num += 1
    #
    #     return res


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
