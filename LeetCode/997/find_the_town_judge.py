class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_noone_set = set(range(1, n+1))
        trusted_by_dict = defaultdict(lambda: 0)

        for people in trust:
            if people[0] in trust_noone_set:
                trust_noone_set.remove(people[0])
            trusted_by_dict[people[1]] += 1

        judge = -1
        for potential_judge in trust_noone_set:
            if trusted_by_dict[potential_judge] == n - 1:
                if judge == -1:
                    judge = potential_judge
                else:
                    return -1

        return judge




class MyTestCase(unittest.TestCase):

    def test1(self):
        n = 2
        trust = [[1, 2]]
        self.assertEqual(2, Solution().findJudge(n, trust))

    def test2(self):
        n = 3
        trust = [[1, 3],[2,3]]
        self.assertEqual(3, Solution().findJudge(n, trust))

    def test3(self):
        n = 3
        trust = [[1, 3], [2, 3], [3, 1]]
        self.assertEqual(-1, Solution().findJudge(n, trust))

    def test4(self):
        n = 3
        trust = [[1, 3], [2, 3]]
        self.assertEqual(3, Solution().findJudge(n, trust))