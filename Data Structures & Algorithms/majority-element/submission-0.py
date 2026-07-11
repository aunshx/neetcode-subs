class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = {}
        for i, val in enumerate(nums):
            s[val] = s.get(val, 0) + 1
        for val in s:
            if s[val] >= len(nums)/2:
                return val

        return maxi