class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        res = r

        def canBeShipped(mid):
            totalDays = 1
            currTotal = 0

            for n in weights:
                if currTotal + n > mid:
                    totalDays += 1
                    currTotal = n
                else:
                    currTotal += n

            return totalDays <= days

        while l <= r:
            mid = (r+l)//2
            if canBeShipped(mid):
                res = min(res,mid)
                r = mid - 1
            else:
                l = mid + 1

        return res