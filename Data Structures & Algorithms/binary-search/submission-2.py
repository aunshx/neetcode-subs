class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1

        while l <= r:
            mid = (r+l)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l += 1
            else:
                r -= 1
        return -1