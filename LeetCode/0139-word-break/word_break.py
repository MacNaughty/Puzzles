import unittest


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        len_s = len(s)
        word_set = set(wordDict)
        # Find the maximum word length to avoid checking impossibly long slices
        max_len = max((len(w) for w in word_set), default=0)
        visited = set()

        def dfs(i: int):
            if i == len_s:
                return True
            if i in visited:
                return False

            # Instead of looping through all words, loop through possible lengths
            for j in range(i + 1, min(i + max_len + 1, len_s + 1)):
                if s[i:j] in word_set:
                    if dfs(j):
                        return True

            visited.add(i)
            return False

        return dfs(0)




    # def wordBreak(self, s: str, wordDict: list[str]) -> bool:
    #     len_s = len(s)
    #     res = False
    #
    #     for word1 in wordDict:
    #         i = 0
    #         len_word1 = len(word1)
    #         if len_word1 > len_s or s[i:i + len_word1] != word1:
    #             continue
    #
    #         i += len_word1
    #         has_word = False
    #         while True:
    #             # TODO: this needs a path of indices
    #             j = i
    #             for word in wordDict:
    #                 len_word = len(word)
    #                 if j+len_word <= len_s and s[j:j+len_word] == word:
    #                     j += len_word
    #                     has_word = True
    #                     break
    #
    #             if j == len_s:
    #                 return True
    #
    #             if has_word:
    #                 has_word = False
    #             else:
    #                 break
    #
    #     return res

class MyTestCase(unittest.TestCase):
    def test_1(self):
        s = "leetcode"
        wordDict = ["leet","code"]
        expected = True
        actual = Solution().wordBreak(s, wordDict)
        self.assertEqual(expected, actual)

    def test_2(self):
        s = "applepenapple"
        wordDict = ["apple","pen"]
        expected = True
        actual = Solution().wordBreak(s, wordDict)
        self.assertEqual(expected, actual)

    def test_3(self):
        s = "catsandog"
        wordDict = ["cats","dog","sand","and","cat"]
        expected = False
        actual = Solution().wordBreak(s, wordDict)
        self.assertEqual(expected, actual)

    def test_4(self):
        s = "a"
        wordDict = ["b"]
        expected = False
        actual = Solution().wordBreak(s, wordDict)
        self.assertEqual(expected, actual)

    def test_5(self):
        s = "catsandogcat"
        wordDict = ["cats","dog","sand","and","cat","an"]
        expected = True
        actual = Solution().wordBreak(s, wordDict)
        self.assertEqual(expected, actual)

    def test_6(self):
        s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
        wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
        expected = False
        actual = Solution().wordBreak(s, wordDict)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
