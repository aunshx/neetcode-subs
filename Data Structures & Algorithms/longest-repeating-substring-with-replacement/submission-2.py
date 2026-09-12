class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        maxLen = 0
        maxF = 0
        i,j=0,0

        while j < len(s):
            window[s[j]] = window.get(s[j],0) + 1
            maxF = max(maxF, window[s[j]])
            if (j-i+1) - maxF > k:
                window[s[i]] -= 1
                i += 1
            maxLen = max(maxLen, j-i+1)
            j += 1
        return maxLen
                