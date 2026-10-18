class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r,minLength,n,total = 0,0,float('inf'),len(nums),0

        while r < n:
            total += nums[r]
            while total >= target:
                minLength=min(minLength, r-l+1)
                total -= nums[l]
                l += 1
            r += 1

        return minLength if minLength != float('inf') else 0