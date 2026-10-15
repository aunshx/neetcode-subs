class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = set(nums)
        maxLength = 0

        for n in nums:
            if (n-1) not in count:
                length = 0
                curr = n
                while curr in count:
                    curr += 1
                    length += 1
                maxLength = max(maxLength, length)

        return maxLength