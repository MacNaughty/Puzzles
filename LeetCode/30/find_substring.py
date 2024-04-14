import itertools
import unittest
from copy import copy
from typing import List


class Solution:

    # def findSubstring(self, s: str, words: list[str]) -> list[int]:
    #     if len(s) == 1 and len(words) == 1:
    #         return [0] if words[0] == s else []
    #
    #     res = []
    #     concatenated_string_set = set()
    #     temp = itertools.permutations(words)
    #
    #     for permutation in temp:
    #         concatenated_string_set.add(''.join(permutation))
    #
    #     permutation_length = len(next(iter(concatenated_string_set)))
    #
    #     if len(s) < permutation_length:
    #         return []
    #
    #     for i in range(0, len(s) - permutation_length + 1):
    #         if s[i:i+permutation_length] in concatenated_string_set:
    #             res.append(i)
    #
    #     return res


    # def findSubstring(self, s: str, words: List[str]) -> List[int]:
    #     concatenated_string_set = set()
    #
    #     concatenated_string_list = [[words[0]]]
    #     for i in range(1, len(words)):
    #
    #         for j in range(len(concatenated_string_list[:])):
    #             intermediate_concat_list = concatenated_string_list[j]
    #             intermediate_concat_list_copy = copy(intermediate_concat_list)
    #             for k in range(len(intermediate_concat_list[:])):
    #                 # TODO: build copy with inserted item in one go
    #
    #                 intermediate_concat_list.insert(k, words[i])
    #
    #             intermediate_concat_list_copy.append(words[i])
    #             concatenated_string_list.append(intermediate_concat_list_copy)
    #
    #     print()
    #
    #
    #
    #
    #
    #     return []


class MyTestCase(unittest.TestCase):
    def test_1(self):
        s = "barfoothefoobarman"
        words = ["foo","bar"]
        self.assertEqual(Solution().findSubstring(s, words), [0,9])

    def test_2(self):
        s = "wordgoodgoodgoodbestword"
        words = ["word","good","best","word"]
        self.assertEqual(Solution().findSubstring(s, words), [])

    def test_3(self):
        s = "barfoofoobarthefoobarman"
        words = ["bar","foo","the"]
        self.assertEqual(Solution().findSubstring(s, words), [6,9,12])

    def test_4(self):
        s = "wordgoodgoodgoodbestword"
        words = ["word","good","best","good"]
        self.assertEqual(Solution().findSubstring(s, words), [8])

    def test_5(self):
        s = "pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel"
        words = ["dhvf","sind","ffsl","yekr","zwzq","kpeo","cila","tfty","modg","ztjg","ybty","heqg","cpwo","gdcj","lnle","sefg","vimw","bxcb"]
        self.assertEqual(Solution().findSubstring(s, words), [8])

if __name__ == '__main__':
    unittest.main()
