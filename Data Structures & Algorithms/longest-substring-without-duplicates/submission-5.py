class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        l,r=0,0
        ans = 0
        while r < len(s):
            m[s[r]] = m.get(s[r],0) + 1
            while m[s[r]] > 1:
                m[s[l]] -= 1
                if m[s[l]] == 0:
                    del m[s[l]]
                l += 1
            r += 1
            ans = max(ans, r-l)
        return ans