class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for n in nums:
            index = abs(n) - 1
            if nums[index-1] < 0:
                return abs(n)
            nums[index-1] *= -1
        return -1