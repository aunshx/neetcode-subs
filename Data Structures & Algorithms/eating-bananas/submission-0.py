import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canEat(eatingRate):
            currSum = 0            
            for p in piles:
                currSum += math.ceil(p/eatingRate)
            return currSum <= h

          
        l = 1
        r = max(piles)
        res = r
        while l<=r:
            mid = l + (r-l)//2
            if canEat(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res 
