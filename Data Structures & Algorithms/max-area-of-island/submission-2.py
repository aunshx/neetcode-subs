class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
        maxArea = 0

        def dfs(r,c):
            if min(r,c) < 0 or r >= ROWS or c >= COLS or visited[r][c] or grid[r][c] == 0:
                return 0

            visited[r][c] = True
            value = 1
            for mr, mc in DIRECTIONS:
                value += dfs(mr+r,mc+c)

            return value
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    value = dfs(r,c)
                    maxArea = max(maxArea, value)

        return maxArea