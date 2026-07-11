class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expectedSum = (len(nums)*(len(nums)+1))//2
        arrSum = sum(nums) 

        print(expectedSum, arrSum)
        
        return expectedSum - arrSum 
        