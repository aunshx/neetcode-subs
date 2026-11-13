class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        l = 0
        r = ROWS - 1

        while l<r:
            mid = (r+l)//2

            if target <= matrix[mid][COLS-1]:
                r = mid 
            else:
                l = mid + 1

        row = matrix[l]
        l=0
        r = COLS-1

        while l<=r:
            mid = (r+l)//2

            if target == row[mid]:
                return True
            elif target < row[mid]:
                r = mid - 1
            else:
                l = mid + 1

        return False
