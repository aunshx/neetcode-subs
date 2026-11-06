class Solution:
    def merge(self,a,b):
        i,j=0,0
        n = len(a)
        m = len(b)
        res = []

        while i < n and j < m:
            if a[i] > b[j]:
                res.append(b[j])
                j += 1
            else:
                res.append(a[i])
                i += 1

        res.extend(b[j:] if j < m else a[i:])

        return res
    
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums 
        mid = len(nums)//2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        return self.merge(left, right)