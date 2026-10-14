class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
        DIRECTIONS = [(0,1),(1,0),(0,-1),(-1,0)]
        count = 0

        def dfs(r, c):
            nonlocal count
            if min(r,c) < 0 or r >= ROWS or c >= COLS or visited[r][c] or grid[r][c] == '0':
                return 
            visited[r][c] = True
            for mr, mc in DIRECTIONS:
                dfs(r+mr, c+mc)
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and not visited[r][c]:
                    dfs(r, c)
                    count += 1

        return count
