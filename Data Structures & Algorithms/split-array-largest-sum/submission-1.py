class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = max(nums)
        r = sum(nums)
        res = r

        def canBeSplit(mid):
            totalSum = 0
            totalSplits = 1
            for n in nums:
                if totalSum + n > mid:
                    totalSplits += 1
                    totalSum = n
                else:
                    totalSum += n

            return totalSplits <= k

        while l<r:
            mid = (r+l)//2

            if canBeSplit(mid):
                r = mid
                res = min(res,mid)
            else:
                l = mid + 1

        return res