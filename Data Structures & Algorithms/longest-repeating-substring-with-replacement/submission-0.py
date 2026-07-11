class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        max_len = 0
        max_freq = 0
        l,r=0,0
        while r < len(s):
            mp[s[r]] = mp.get(s[r],0) + 1
            max_freq = max(max_freq, mp[s[r]])

            while r-l+1 - max_freq > k:
                mp[s[l]] -= 1
                l += 1
            max_len = max(max_len, r-l+1)
            r += 1
        return max_len