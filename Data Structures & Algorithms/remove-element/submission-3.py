class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l,r,n=0,0,len(nums)

        while r < n:
            while r < n and nums[r] == val:
                r += 1
            if r < n:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
                r += 1

        return l