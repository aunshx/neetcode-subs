class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        visited = set()
        res = []

        def permute(path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if i in visited:
                    continue
                if i > 0 and nums[i] == nums[i-1] and (i-1) not in visited:
                    continue
                visited.add(i)
                path.append(nums[i])
                permute(path)
                visited.remove(i)
                path.pop()

        permute([])
        return res
