class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1,count2 = 0,0
        candidate1,candidate2 = None, None

        for n in nums:
            if candidate1 is not None and n == candidate1:
                count1 += 1
            elif candidate2 is not None and n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 += 1
            elif count2 == 0:
                candidate2 = n
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        return [c for c in (candidate1, candidate2) if nums.count(c) > len(nums)//3]


        