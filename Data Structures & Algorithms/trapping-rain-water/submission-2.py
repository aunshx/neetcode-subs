class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]
        total = 0
        while l < r:
            if maxLeft < maxRight:
                l += 1
                total += max(0, maxLeft - height[l])
                maxLeft = max(maxLeft, height[l])
            else:
                r -= 1
                total += max(0, maxRight - height[r])
                maxRight = max(maxRight, height[r])
        return total