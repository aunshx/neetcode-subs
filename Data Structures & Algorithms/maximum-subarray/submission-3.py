class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l,r=0,0
        n = len(nums)
        total = 0
        maxTotal = float('-inf')
        while r < n:
            total += nums[r]
            maxTotal = max(maxTotal, total)
            while total < 0:
                total -= nums[l]
                l += 1
            r += 1
        return maxTotal
