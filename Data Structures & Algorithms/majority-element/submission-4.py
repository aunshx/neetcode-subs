class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None

        for n in nums:
            if candidate == n:
                count += 1
            elif count == 0:
                candidate = n
                count = 1
            else:
                count -= 1

        return candidate
