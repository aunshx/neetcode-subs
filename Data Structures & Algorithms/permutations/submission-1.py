class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        res = []

        def permute(path):
            if len(path) == len(nums):
                res.append(path[:])
                return 

            for i in range(len(nums)):
                if i in visited:
                    continue
                visited.add(i)
                path.append(nums[i])
                permute(path)
                visited.remove(i)
                path.pop()

        permute([])
        return res