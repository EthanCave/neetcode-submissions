class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = [set() for _ in range(9)]
        for row in range(len(board)):
            for col in range(len(board[row])):
                val = board[row][col]
                if val == ".":
                    continue
                grid = (row // 3) * 3 + col // 3
                if val in rows[row] or val in cols[col] or val in grids[grid]:
                    return False
                rows[row].add(val)
                cols[col].add(val)
                grids[grid].add(val)
        return True