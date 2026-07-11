class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            self.prefix.append(total)
        

    def sumRange(self, left: int, right: int) -> int:
        prefixRight = self.prefix[right]
        prefixLeft = self.prefix[left-1] if left > 0 else 0
        return prefixRight-prefixLeft


        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)