class Solution:
    def dfs(self, grid, r, c, visit, ROWS, COLS):
        if (min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] == '0'):
            return 
        
        visit.add((r,c))
        neighbours = [(0,1),(1,0),(-1,0),(0,-1)]
        for dr, dc in neighbours:
            self.dfs(grid, r + dr, c + dc, visit, ROWS, COLS)

        return 

    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visit:
                    count += 1  
                    self.dfs(grid, r, c, visit, ROWS, COLS)
        return count