class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [0] * n
        postfix = [0] * n
        prefix[0] = height[0]
        for i in range(1, n):
            prefix[i] = max(height[i], prefix[i-1])

        postfix[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            postfix[i] = max(height[i], postfix[i+1])
        
        water = 0

        for i in range(1,n-1):
            water += min(prefix[i], postfix[i])- height[i]
        return water