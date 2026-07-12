class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = [[nums[0]]]
        for num in nums[1:]:
            new_res = res.copy()

            new_res.append([num])

            for e in res:
                new_res += [e + [num]]

            res = new_res

        return [[]] + res
