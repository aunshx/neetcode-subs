class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        totalXOR = 0

        def backtrack(i, currXOR):
            nonlocal totalXOR
            if i == len(nums):
                totalXOR += currXOR
                return 
            backtrack(i+1, currXOR^nums[i])

            backtrack(i+1, currXOR)

        backtrack(0,0)
        return totalXOR