class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 1:
            return ''

        base = strs[0]
        ans = ""

        for i in range(1, len(strs)):
            minLen = min(len(strs[i]), len(base))
            j = 0
            while j < minLen:
                if strs[i][j] != base[j]:
                    base = base[:j]
                    break
                j += 1
            base = base[:j]


        return base
        
        