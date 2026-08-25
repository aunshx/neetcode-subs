class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left,right=0,len(heights)-1

        maxArea = 0

        while left<right:
            maxArea = max(maxArea, min(heights[left], heights[right])*(right-left))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                
        return maxArea
