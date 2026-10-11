class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l,r=0,0
        w1,w2=len(word1),len(word2)
        arr = []
        while l < w1 and r < w2:
            arr.append(word1[l])
            arr.append(word2[r])
            l += 1
            r += 1
        arr.extend(word1[l:]) if l < w1 else arr.extend(word2[r:])
        return ''.join(arr)