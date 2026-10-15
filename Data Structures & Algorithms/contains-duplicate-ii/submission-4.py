class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = {}
        for i,num in enumerate(nums):
            diff = k - num
            if diff in n and abs(n[diff]-i) <= k:
                return True
            n[diff] = i

        return False