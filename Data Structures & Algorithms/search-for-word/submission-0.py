class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        visited = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        def backtrack(i,j,k):
            if k == len(word):
                return True 
            if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                return False
            if visited[i][j] == 1:
                return False
            if board[i][j] != word[k]:
                return False

            visited[i][j] = 1
            if backtrack(i+1,j,k+1):
                return True
            if backtrack(i-1,j,k+1):
                return True
            if backtrack(i,j+1,k+1):
                return True
            if backtrack(i,j-1,k+1):
                return True
            visited[i][j] = 0
            return False


        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    if backtrack(i,j,0):
                        return True

        return False