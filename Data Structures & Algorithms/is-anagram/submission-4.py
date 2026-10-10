class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1, t1 = len(s), len(t)
        if s1 != t1:
            return False
        countS = {}

        for c in s:
            countS[c] = countS.get(c,0) + 1
        for c in t:
            countS[c] = countS.get(c,0) - 1

        return all(v == 0 for v in countS.values())