class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def permute(i, path):
            if i == len(nums):
                res.append(path[:])
                return 

            for num in nums:
                if num in path:
                    continue
                path.append(num)
                permute(i+1, path)
                path.pop()

        permute(0,[])
        return res
            