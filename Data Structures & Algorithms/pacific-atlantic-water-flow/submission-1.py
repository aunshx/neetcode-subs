class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac = set()
        atl = set()
        neighbours = [(0,1),(1,0),(-1,0),(0,-1)]
        result = []

        def dfs(r,c,prevHeight,visit):
            if (min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visit or prevHeight > heights[r][c]):
                return 
            visit.add((r,c))
            for dr, dc in neighbours:
                dfs(r + dr, c + dc, heights[r][c], visit)


        for c in range(COLS):
            dfs(0, c, heights[0][c], pac)        # top edge → Pacific
        for r in range(ROWS):
            dfs(r, 0, heights[r][0], pac)        # left edge → Pacific
        for c in range(COLS):
            dfs(ROWS-1, c, heights[ROWS-1][c], atl)   # bottom edge → Atlantic
        for r in range(ROWS):
            dfs(r, COLS-1, heights[r][COLS-1], atl)   # right edge → Atlantic

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    result.append([r,c])

        return result