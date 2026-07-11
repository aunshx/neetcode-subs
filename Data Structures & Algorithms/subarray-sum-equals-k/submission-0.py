class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {
            0 : 1
        }

        res = currSum = 0
        for i in range(len(nums)):
            currSum += nums[i]
            # I don't get the below 
            diff = currSum - k
            res += prefixSum.get(diff, 0)
            prefixSum[currSum] = 1 + prefixSum.get(currSum,0)

        return res
