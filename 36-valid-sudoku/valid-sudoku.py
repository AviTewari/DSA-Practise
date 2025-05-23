class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        col = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                else:
                    if (board[r][c] in rows[r] or
                        board[r][c] in col[c] or
                        board[r][c] in squares[(r//3,c//3)]):
                        return False
                rows[r].add(board[r][c])
                col[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True
