class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_count = float('inf')
        r,l=0,0

        while r < len(nums):
            target -= nums[r]
            while target <= 0:
                min_count = min(min_count, r-l+1)
                target += nums[l]
                l += 1
            r += 1
        
        return 0 if min_count == float('inf') else min_count
