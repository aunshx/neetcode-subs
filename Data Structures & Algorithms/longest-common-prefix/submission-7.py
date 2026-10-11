class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        i = 1
        while i<len(strs):
            prefix = prefix[:len(strs[i])]
            for j in range(len(strs[i])):
                if j < len(prefix) and strs[i][j] != prefix[j]:
                    prefix = prefix[:j]
                    break
            i += 1
        return prefix