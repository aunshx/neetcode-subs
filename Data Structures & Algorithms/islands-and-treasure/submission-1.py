class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS, DIR = len(grid),len(grid[0]),[(0,1),(1,0),(0,-1),(-1,0)]
        q = deque()
        INF = 2147483647

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        dist = 1
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                for mr, mc in DIR:
                    row,col = mr+r, mc+c
                    if (0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 2147483647):
                        grid[row][col] = dist
                        q.append((row,col))
            dist += 1
