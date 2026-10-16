class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        maxLength = 0
        for n in nums:
            if (n-1) not in store:
                length = 0
                while n in store:
                    n += 1
                    length += 1
                maxLength = max(maxLength, length)

        return maxLength