class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0] * (n*2)
        for i, val in enumerate(nums):
            arr[i] = val
            arr[i+n] = val

        return arr