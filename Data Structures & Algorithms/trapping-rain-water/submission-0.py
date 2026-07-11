class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxLeft = 0
        maxRight = 0
        i,j=0,n-1
        maxLeftArr = [0] * n
        maxRightArr = [0] * n
        while i < n:
            maxLeftArr[i] = maxLeft
            maxRightArr[n-i-1] = maxRight

            maxLeft = max(maxLeft, height[i])
            maxRight = max(maxRight, height[n-i-1])
            i += 1
            j -= 1
        total = 0
        for i in range(n):
            total += max(0, min(maxRightArr[i],maxLeftArr[i]) - height[i])

        return total
            
            



        


        