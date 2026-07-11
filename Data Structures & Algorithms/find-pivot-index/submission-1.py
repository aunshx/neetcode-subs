class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * n
        postfix = [0] * n

        for i in range(1, n):
            prefix[i] = prefix[i-1] + nums[i-1]

        for i in range(n-2, -1, -1):
            postfix[i] = postfix[i+1] + nums[i+1]

        for i in range(n):
            if prefix[i] == postfix[i]:
                return i

        return -1
