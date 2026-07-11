class Solution:
    def sortColors(self, nums: List[int]) -> None:
        one, two, three = 0,0,0

        for num in nums:
            if num == 0:
                one += 1
            elif num == 1:
                two += 1
            else:
                three += 1
        print(one, two, three, nums)
        i=0
        while i<one:
            nums[i] = 0
            i += 1
        while i<one+two:
            nums[i] = 1
            i += 1
        while i<one+two+three:
            nums[i] = 2
            i += 1
        

        