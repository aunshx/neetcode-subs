class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        DIR = [(0,1),(1,0),(-1,0),(0,-1)]

        def dfs(r,c,k):
            if k == len(word):
                return True

            if min(r,c) < 0 or r >= ROWS or c >= COLS or (r,c) in visited or board[r][c] != word[k]:
                return False

            visited.add((r,c))
            for mr, mc in DIR:
                if dfs(r+mr, c+mc, k+1):
                    return True
            visited.remove((r,c))
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True

        return False