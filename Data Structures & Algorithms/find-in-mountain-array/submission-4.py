class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()

        if n < 3:
            return -1 

        l = 1
        r = n-2

        while l <= r:
            mid = (r+l)//2
            val = mountainArr.get(mid)
            right = mountainArr.get(mid+1)
            left = mountainArr.get(mid-1)
            if left < val < right:
                l = mid + 1
            elif left > val > right:
                r = mid - 1
            else:
                break

        peak = mid

        l=0
        r=peak-1

        while l<=r:
            mid = (r+l)//2
            val = mountainArr.get(mid)

            if target == val:
                return mid
            elif target < val:
                r = mid - 1
            else:
                l = mid + 1


        l=peak
        r=n-1

        while l<=r:
            mid = (r+l)//2
            val = mountainArr.get(mid)

            if target == val:
                return mid
            elif target < val:
                l = mid + 1
            else:
                r = mid - 1

        return -1

