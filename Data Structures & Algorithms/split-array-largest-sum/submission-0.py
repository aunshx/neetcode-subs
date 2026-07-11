class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def canMinimizeSum(largest):
            currSum = 0
            splitWays = 1

            for n in nums:
                currSum += n
                if currSum > largest:
                    splitWays += 1
                    currSum = n
            
            return splitWays <= k
        
        l = max(nums)
        r = sum(nums)
        res = r

        while l<=r:
            mid = l + (r-l)//2

            if canMinimizeSum(mid):
                res = mid 
                r = mid - 1
            else:
                l = mid + 1

        return res 