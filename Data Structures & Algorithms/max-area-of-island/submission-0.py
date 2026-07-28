class Solution:
    def dfs(self, grid, r, c, visit, ROWS, COLS):
        if (min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] == 0):
            return 0

        visit.add((r,c))
        size = 1
        neighbours = [(0,1),(1,0),(0,-1),(-1,0)]

        for dr, dc in neighbours:
            size += self.dfs(grid, r + dr, c + dc, visit, ROWS, COLS)

        return size

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        maxArea = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visit:
                    maxArea = max(maxArea, self.dfs(grid, r, c, visit, ROWS, COLS))
        return maxArea