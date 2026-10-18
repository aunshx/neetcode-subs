class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
        DIRECTIONS = [(0,1),(1,0),(0,-1),(-1,0)]

        def dfs(r, c):
            if min(r,c) < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
                return 1

            if visited[r][c]:
                return 0

            visited[r][c] = True

            perimeter = 0
            for mr, mc in DIRECTIONS:
                perimeter += dfs(r+mr, c+mc)

            return perimeter
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r, c)

        return 0       