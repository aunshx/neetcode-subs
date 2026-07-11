class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, curr, total):
            if total > target:
                return 

            if total == target:
                res.append(curr.copy())
                return 

            if index >= len(nums):
                return 

            curr.append(nums[index])

            dfs(index, curr, total+nums[index])
            curr.pop()
            dfs(index+1, curr, total)

        dfs(0, [], 0)
        return res