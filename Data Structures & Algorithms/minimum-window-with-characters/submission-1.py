class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}

        for ch in t:
            need[ch] = need.get(ch,0) + 1

        window = {}
        required = len(need)
        bestLen = float('inf')
        have = 0
        l = 0
        r = 0
        best = (0,0)

        while r < len(s):
            ch = s[r]
            window[ch] = window.get(ch,0)+1

            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == required:
                if r-l+1 < bestLen:
                    bestLen = r-l+1
                    best = (l,r)

                d = s[l]
                window[d] -= 1
                if d in need and window[d] < need[d]:
                    have -= 1

                l += 1
            r += 1

        l,r = best
        return s[l:r+1] if bestLen != float('inf') else ''






