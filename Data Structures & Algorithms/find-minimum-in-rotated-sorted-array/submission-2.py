class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l,r=0,n-1
        while l<r:
            mid = l + (r-l)//2
            if nums[r] > nums[mid]:
                r = mid
            else:
                l = mid + 1


        return nums[l]