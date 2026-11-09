class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        val1, val2 = None, None
        count1, count2 = 0, 0
        
        for n in nums:
            if n == val1:
                count1 += 1
            elif n == val2:
                count2 += 1
            elif count1 == 0:
                val1 = n
                count1 = 1
            elif count2 == 0:
                val2 = n
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
                
        res = []
        for val in [val1, val2]:
            if val is not None and nums.count(val) > len(nums) // 3 and val not in res:
                res.append(val)
        return res