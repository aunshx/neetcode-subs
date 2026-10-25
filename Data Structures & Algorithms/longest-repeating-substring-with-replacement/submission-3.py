class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        i,j,n=0,0,len(s)
        maxFrequency = 0
        maxLen = 0

        while j<n:
            window[s[j]] = window.get(s[j], 0) + 1
            maxFrequency = max(maxFrequency, window[s[j]])
            if (j-i+1) - maxFrequency > k:
                window[s[i]] -= 1
                i += 1
            maxLen = max(maxLen, j-i+1)
            j += 1

        return maxLen