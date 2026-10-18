class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS, DIR = len(grid), len(grid[0]), [(0,1),(1,0),(-1,0),(0,-1)]
        fresh = 0
        time = 0
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1

        while fresh > 0 and q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for mr, mc in DIR:
                    row, col = mr+r,mc+c
                    if (0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 1):
                        grid[row][col] = 2
                        q.append((row,col))
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1