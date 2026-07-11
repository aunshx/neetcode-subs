class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}
        
        for i in range(len(nums)):
            if nums[i] in mp:
                diff = i - mp[nums[i]]
                if diff <= k:
                    return True
                else:
                    mp[nums[i]] = i
            else:
                mp[nums[i]] = i

        return False