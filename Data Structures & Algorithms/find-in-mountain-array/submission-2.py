class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        l,r=0,n-1
        # Find the peak
        while l<r:
            mid = l + (r-l)//2
            midVal = mountainArr.get(mid)
            midValNext = mountainArr.get(mid+1)
            #Still Climbing
            if midVal < midValNext:
                l = mid + 1
            else:
                r = mid
        peak = l

        l,r=0,peak
        # Search in Left 
        while l<=r:
            mid = l + (r-l)//2
            midVal = mountainArr.get(mid)
            if target == midVal:
                return mid
            elif midVal < target:
                l = mid + 1
            else:
                r = mid - 1
        # Search in Right
        l,r=peak+1,n-1
        while l<=r:
            mid = l + (r-l)//2
            midVal = mountainArr.get(mid)
            if target == midVal:
                return mid
            elif midVal > target:
                l = mid + 1
            else:
                r = mid - 1


        return -1
