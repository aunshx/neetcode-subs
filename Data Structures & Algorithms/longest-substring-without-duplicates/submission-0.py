class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        char_to_idx = {}

        l,r=0,0
        res = 0
        while r<len(s):
            if s[r] in char_to_idx:
                l = max(char_to_idx[s[r]] + 1, l)
            char_to_idx[s[r]] = r
            res = max(res, r-l+1)
            r += 1
        
        return res