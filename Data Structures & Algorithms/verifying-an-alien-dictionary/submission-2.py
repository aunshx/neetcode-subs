class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        m = {c:i for i,c in enumerate(order)}

        for i in range(1,len(words)):
            w1,w2 = words[i-1],words[i]

            for j in range(len(w1)):
                if j == len(w2):
                    return False

                if w1[j] != w2[j]:
                    if m[w1[j]] > m[w2[j]]:
                        return False 
                    break

        return True