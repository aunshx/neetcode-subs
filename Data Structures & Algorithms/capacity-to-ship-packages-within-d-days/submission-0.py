class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def isCapacity(largest):
            currSum = 0
            k = 1
            for w in weights:
                currSum += w
                if currSum > largest:
                    k += 1
                    currSum = w
            
            return k <= days
        
        l = max(weights)
        r = sum(weights)
        res = r
        while l<=r:
            mid = l + (r-l)//2

            if isCapacity(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res