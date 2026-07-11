class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        l,r = 0,ROWS-1
        currClosest = 0
        while l <= r:
            mid = l + (r-l)//2
            currClosest = matrix[mid][0]
            if target == currClosest:
                return True
            elif target < currClosest:
                r = mid - 1
            else:
                l = mid + 1

        arr = matrix[(r+l)//2]
        left,right=0,COLS-1


        while left<=right:
            mid = left + (right-left)//2
            if target == arr[mid]:
                return True
            elif target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        

        return False 
        