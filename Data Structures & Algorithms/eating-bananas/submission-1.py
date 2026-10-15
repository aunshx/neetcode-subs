class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Min and Max bananas we can eat
        l,r=1,max(piles)
        res = 0
        while l<=r:
            mid = l + (r-l)//2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p/mid)
            if totalTime <= h:
                r = mid - 1
                res = mid
            else:
                l = mid + 1
        return res
