class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}
        total = 0
        count = 0
        for n in nums:
            total += n
            if total-k in prefix:
                count += prefix[total-k]
            prefix[total] = prefix.get(total, 0) + 1
        return count