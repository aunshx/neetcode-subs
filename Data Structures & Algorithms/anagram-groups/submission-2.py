class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        ans = []
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            k = tuple(key)
            if k not in m:
                m[k] = []
            m[k].append(s)
        
        for k,v in m.items():
            ans.append(v)
            
        return ans