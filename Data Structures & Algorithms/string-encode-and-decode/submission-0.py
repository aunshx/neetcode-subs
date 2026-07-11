class Solution:
    def encode(self, strs: List[str]) -> str:
        encode = ''
        for i,val in enumerate(strs):
            encode += str(len(val)) + '#' + val
        return encode

    def decode(self, s: str) -> List[str]:
        decode = []
        i = 0
        while i < len(s):
            num = ''
            while s[i] != '#':
                num += s[i]
                i += 1
            i += 1
            r = int(num)
            res = ''
            for _ in range(r):
                res += s[i]
                i += 1
            decode.append(res)
        return decode