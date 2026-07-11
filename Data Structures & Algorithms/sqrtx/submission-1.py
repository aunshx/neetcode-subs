class Solution:
    def mySqrt(self, x: int) -> int:
        l,r=0,x
        nearestSqr = 0
        while l<=r:
            mid = (r+l)//2

            val = mid*mid
            if val == x:
                return mid
            elif val < x:
                nearestSqr = mid
                l = mid + 1
            else:
                r = mid - 1
            nearestSqr = min(nearestSqr, mid)
    
        return nearestSqr

            