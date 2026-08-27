class Solution:
    def merge(self, w1, w2, res, i):
        while i < len(w2):
            res.append(w1[i])
            res.append(w2[i])
            i += 1
        return i

    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1,n2=len(word1),len(word2)

        res = []
        i = 0
        if n1 >= n2:
            i = self.merge(word1, word2, res, i)
            res.extend(word1[i:])
        else:
            i = self.merge(word1, word2[:n1], res, i)
            res.extend(word2[i:])

        return ''.join(res)