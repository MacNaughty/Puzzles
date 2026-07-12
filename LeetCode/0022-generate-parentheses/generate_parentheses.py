class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]

        res = []

        def next_permutations(paren_string: str, paren_count, open_paren_acc):
            if open_paren_acc == n:
                while paren_count > 0:
                    paren_string += ')'
                    paren_count -= 1
                res.append(paren_string)
            else:
                if paren_count > 0:
                    next_permutations(paren_string + '(', paren_count + 1, open_paren_acc + 1)
                    next_permutations(paren_string + ')', paren_count - 1, open_paren_acc)
                else:
                    next_permutations(paren_string + '(', paren_count + 1, open_paren_acc + 1)

        next_permutations('(', 1, 1)

        return res
