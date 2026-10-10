class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            diff = target-nums[i]
            if nums[i] in m:
                return [m[nums[i]],i]
            m[diff] = i

        return [0,0]