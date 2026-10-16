class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_by = [0] * (n + 1)
        trust_count = [0] * (n + 1)

        for x,y in trust:
            trusted_by[x] += 1
            trust_count[y] += 1

        i = 1
        while i < n+1:
            if trusted_by[i] == 0 and trust_count[i] == n-1:
                return i
            i += 1

        return -1