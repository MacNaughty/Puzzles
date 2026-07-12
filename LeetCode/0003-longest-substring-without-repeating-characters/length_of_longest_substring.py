class Solution:

    @staticmethod
    def length_of_longest_substring(s: str) -> int:
        len_s = len(s)
        if len_s == 0:
            return 0

        res = 1
        s_charlist = list(s)

        i = 0
        while i < len_s and res < len_s - i:
            curr_chars = {s_charlist[i]}
            temp_res = 1

            j = i+1
            while j < len_s and s_charlist[j] not in curr_chars:
                curr_chars.add(s_charlist[j])
                temp_res += 1
                j += 1

            res = max(temp_res, res)
            i += 1

        return res


class MyTestCase(unittest.TestCase):

    def test_1(self):
        s = "abcabcbb"
        self.assertEqual(3, Solution.length_of_longest_substring(s))

    def test_2(self):
        s = "bbbbb"
        self.assertEqual(1, Solution.length_of_longest_substring(s))

    def test_3(self):
        s = "pwwkew"
        self.assertEqual(3, Solution.length_of_longest_substring(s))


if __name__ == '__main__':
    unittest.main()
