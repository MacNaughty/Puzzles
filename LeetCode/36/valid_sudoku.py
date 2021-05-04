class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column_nums = {
            0: set(),
            1: set(),
            2: set(),
            3: set(),
            4: set(),
            5: set(),
            6: set(),
            7: set(),
            8: set(),
        }
        square_nums = {
            (0, 0): set(),
            (0, 1): set(),
            (0, 2): set(),
            (1, 0): set(),
            (1, 1): set(),
            (1, 2): set(),
            (2, 0): set(),
            (2, 1): set(),
            (2, 2): set(),
        }

        for i, row in enumerate(board):
            column_square_key = i // 3
            row_nums = set()
            for j, e in enumerate(row):
                row_square_key = j // 3
                if e in column_nums[j] or e in row_nums or e in square_nums[(column_square_key, row_square_key)]:
                    return False
                elif e != ".":
                    column_nums[j].add(e)
                    row_nums.add(e)
                    square_nums[(column_square_key, row_square_key)].add(e)

        return True
