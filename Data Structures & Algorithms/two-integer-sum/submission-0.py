class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        res = []
        for i, val in enumerate(nums):
            diff = target - nums[i]
            if diff in s:
                res.extend([s.get(diff),i])
            else:
                s[val] = i
        return res