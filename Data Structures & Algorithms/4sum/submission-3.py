class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        if n < 4:
            return res
        for i in range(n):    
            if i > 0 and nums[i-1] == nums[i]:
                continue

            for j in range(i+1,n):
                if j > i+1 and nums[j-1] == nums[j]:
                    continue

                k = j + 1
                l = n - 1

                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l] 
                    if total == target:
                        res.append([nums[i],nums[j],nums[k],nums[l]])  
                        k += 1
                        l -= 1

                        while k < l and nums[k] == nums[k-1]:
                            k += 1

                        while k < l and nums[l] == nums[l+1]:
                            l -= 1

                    elif total > target:
                        l -= 1
                    else:
                        k += 1
        return res        
