from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = defaultdict(set)
        COLS = defaultdict(set)
        SQUARES = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                if board[r][c] in ROWS[r] or board[r][c] in COLS[c] or board[r][c] in SQUARES[(r//3,c//3)]:
                    return False
                COLS[c].add(board[r][c])
                ROWS[r].add(board[r][c])
                SQUARES[(r//3,c//3)].add(board[r][c])

        return True

                

