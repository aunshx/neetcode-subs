class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            subset = []
            for r in res:
                subset.append(r + [n])
            res.extend(subset)

        return res
        