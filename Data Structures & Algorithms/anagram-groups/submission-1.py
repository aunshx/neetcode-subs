class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        res = []
        for s in strs:
            ans = [0] * 26
            for ch in s:
                ans[ord(ch)-ord('a')] += 1
            key = tuple(ans)
            if key not in dictionary:
                dictionary[key] = [s]
            else:
                dictionary[key].append(s)

        return list(dictionary.values())