class Solution:
    def dfs(self, grid, r, c, ROWS, COLS, visit):
        if (min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visit or grid[r][c] == 1):
            return 0

        if r == ROWS - 1 and c == COLS - 1:
            return 1

        visit.add((r,c))
        count = 0
        for dr, dc in [(1,0),(0,1),(0,-1),(-1,0)]:
            count += self.dfs(grid,dr + r,dc + c,ROWS,COLS,visit)
        visit.remove((r,c))
        return count

    def countPaths(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        count = 0

        return self.dfs(grid,0,0,ROWS,COLS,visit)