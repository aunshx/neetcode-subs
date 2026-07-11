class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n, i = len(nums), 0
        ans = [0] * (2*n)
        for i, val in enumerate(nums):
            ans[i] = ans[i+n] = val
        return ans

        