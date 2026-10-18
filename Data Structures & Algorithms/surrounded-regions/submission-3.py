class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
        DIR = [(0,1),(1,0),(-1,0),(0,-1)]

        def dfs(r,c):
            if min(r,c) < 0 or r >= ROWS or c >= COLS or visited[r][c] or board[r][c] != 'O':
                return 

            visited[r][c] = True
            board[r][c] = 'T'
                
            for mr,mc in DIR:
                dfs(mr+r,mc+c)

            return 
        
        for r in range(ROWS):
            for c in range(COLS):
                if r == ROWS - 1 or c == COLS - 1 or min(r,c) == 0:
                    if board[r][c] == 'O':
                        dfs(r,c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'