class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visit = set()
        neighbours = [(0,1),(1,0),(0,-1),(-1,0)]

        def dfs(r,c):
            if (min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visit) or board[r][c] == 'X':
                return 

            visit.add((r,c))

            for dr, dc in neighbours:
                dfs(r+dr, c+dc)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r,c) not in visit and (r == ROWS - 1 or c == COLS - 1 or r == 0 or c == 0):
                    dfs(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r,c) not in visit:
                    board[r][c] = 'X'   
            