class Solution:
    def __init__(self):
        self.dial_pad_dict = {
            '2': {'a', 'b', 'c'},
            '3': {'d', 'e', 'f'},
            '4': {'g', 'h', 'i'},
            '5': {'j', 'k', 'l'},
            '6': {'m', 'n', 'o'},
            '7': {'p', 'q', 'r', 's'},
            '8': {'t', 'u', 'v'},
            '9': {'w', 'x', 'y', 'z'},
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        res = []

        for c in self.dial_pad_dict[digits[0]]:
            res.append(c)

        if len(digits) == 1:
            return res

        for i in range(1, len(digits)):
            new_res = []
            dial_pad_chars = self.dial_pad_dict[digits[i]]

            for c in dial_pad_chars:
                for s in res:
                    new_res.append(s + c)

            res = new_res

        return res
