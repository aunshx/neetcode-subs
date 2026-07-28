class Solution:
    def dfs(self, grid, r, c, visit, ROWS, COLS):
        if (r,c) in visit:
            return 0
            
        if (min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0):
            return 1
        
        visit.add((r,c))
        value = 0
        neighbours = [(0,1),(1,0),(-1,0),(0,-1)]
        
        for dr, dc in neighbours:
            value += self.dfs(grid, r + dr, c + dc, visit, ROWS, COLS)

        return value

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        value = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visit:
                    value += self.dfs(grid, r, c, visit, ROWS, COLS)
        
        return value