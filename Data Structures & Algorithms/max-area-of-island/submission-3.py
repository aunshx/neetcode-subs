class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0
        DIR = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

        def dfs(r,c):
            if min(r,c) < 0 or r >= ROWS or c >= COLS or visited[r][c] or grid[r][c] == 0:
                return 0

            area = 1
            visited[r][c] = True

            for mr,mc in DIR:
                area += dfs(mr+r,mc+c)

            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r,c))

        return maxArea

    