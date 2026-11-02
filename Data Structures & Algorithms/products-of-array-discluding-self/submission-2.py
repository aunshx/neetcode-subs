class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * (n+1)
        postfix = [1] * (n+1)

        for i in range(1,n+1):
            prefix[i] = nums[i-1] * prefix[i-1]

        for i in range(n-1,-1,-1):
            postfix[i] = nums[i] * postfix[i+1]

        n = len(prefix)
        res = []
        for i in range(1,n):
            res.append(prefix[i-1]*postfix[i])
        
        return res