class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            n = len(s)
            res += str(n) + '/' + s
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '/':
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:length+j+1])
            i = length + 1 + j                
        return res