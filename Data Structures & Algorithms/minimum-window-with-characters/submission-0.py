class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not t or not s:
            return ""

        need = {}

        for c in t:
            need[c] = need.get(c,0) + 1
        i,j=0,0
        window = {}
        have,total_need = 0,len(need)
        min_len = float("inf")
        result = ''

        while j < len(s):
            c = s[j]
            window[c] = window.get(c, 0) + 1
            if c in need and window[c] == need[c]:
                have += 1

            while have == total_need:
                result_len = j-i+1
                if result_len < min_len:
                    min_len = result_len
                    result = s[i:j+1]
                window[s[i]] -= 1
                if s[i] in need and window[s[i]] < need[s[i]]:
                    have -= 1
                i += 1

            j += 1

        return result
                
