class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        total = 0
        for n in nums:
            total += n
            prefix.append(total)
        total = 0
        postfix = [0] * len(prefix)
        for i in range(len(nums)-1,-1,-1):
            total += nums[i]
            postfix[i] = total
        for i, n in enumerate(nums):
            if prefix[i] == postfix[i]:
                return i
        
        return -1