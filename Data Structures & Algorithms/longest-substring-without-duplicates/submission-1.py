class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        maxLen = 0
        i,j=0,0

        while j < len(s):
            if s[j] in window:
                window.remove(s[i])
                i += 1
            else:
                window.add(s[j])
                j += 1
                maxLen = max(maxLen, j-i)

        return maxLen