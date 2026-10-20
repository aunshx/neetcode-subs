class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def isSubstring(w1, w2):
            if sorted(w1)==sorted(w2):
                return True
            else:
                return False
        
        w= len(s1)
        for i in range(len(s2)):
            if isSubstring(s1, s2[i:i+w]):
                return True
        return False