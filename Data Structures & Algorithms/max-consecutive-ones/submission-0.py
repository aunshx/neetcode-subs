class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr, maxi = 0,0 
        for i, val in enumerate(nums):
            if val == 1:
                curr += 1
                maxi = max(maxi, curr)
            else:
                curr = 0
        return maxi

        