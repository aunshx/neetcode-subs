class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        i = 0
        n = len(nums)
        k %= n
        while k:
            temp = nums[n-1]
            for i in range(n-1,0,-1):
                nums[i] = nums[i-1]
            nums[0] = temp
            k -= 1
        