class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        minVal,maxVal=min(nums),max(nums)
        count = [0]*(maxVal-minVal+1)
        res = []
        for i in range(len(nums)):
            count[nums[i]-minVal] += 1

        for i in range(len(count)):
            for j in range(count[i]):
                res.append(i+minVal)

        return res