class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS = len(image), len(image[0])
        prev_color = image[sr][sc]
        if color == prev_color:
            return image

        def dfs(r,c):
            if (min(r,c) < 0 or r == ROWS or c == COLS or image[r][c] != prev_color):
                return 

            image[r][c] = color

            for dr, dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                dfs(r+dr,c+dc)
            
        
        dfs(sr,sc)
        
        return image
        