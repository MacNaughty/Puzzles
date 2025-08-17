import unittest
from collections import defaultdict


class Solution:

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        candidate_acc_dict = defaultdict(int)
        for candidate in candidates:
            if candidate <= target:
                candidate_acc_dict[candidate] += 1

        can_tuple_list = [(candidate, acc) for candidate, acc in candidate_acc_dict.items()]
        can_tuple_list.sort()

        combo_candidates: list[tuple[list, int]] = []
        for i in range(len(can_tuple_list)):
            candidate, acc = can_tuple_list[i]
            if candidate > target:
                break

            # go through existing combinations and add new candidate
            for combo, combo_sum in combo_candidates[:]:
                acc_i = 1
                while acc_i <= acc and combo_sum + candidate * acc_i < target:
                    combo_candidates.append((combo + [candidate]*acc_i, combo_sum + (candidate * acc_i)))
                    acc_i += 1

                if acc_i <= acc and combo_sum + candidate * acc_i == target:
                    res.append(combo + [candidate]*acc_i)

            # seed combinations with only candidate
            acc_i = 1
            while acc_i <= acc and candidate * acc_i < target:
                combo_candidates.append(([candidate]*acc_i, candidate * acc_i))
                acc_i += 1

            if acc_i <= acc and candidate * acc_i == target:
                res.append([candidate]*acc_i)

        return res


    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()

        def backtrack(start, target, path):
            if target == 0:
                res.append(path)
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                if target < candidates[i]:
                    break

                backtrack(i + 1, target - candidates[i], path + [candidates[i]])

        backtrack(0, target, [])
        return res




class MyTestCase(unittest.TestCase):
    def test_1(self):
        input = [10,1,2,7,6,1,5]
        expected = [
            [1,1,6],
            [1,2,5],
            [1,7],
            [2,6]
        ]
        actual = Solution().combinationSum(input, 8)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
