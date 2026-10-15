class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        maxW = max(people)
        minW = min(people)
        count = [0] * (maxW-minW+1)
        ans = 0

        for p in people:
            count[p-minW] += 1
        res = []
        for i in range(len(count)):
            for _ in range(count[i]):
                res.append(i+minW)

        l,r=0,len(res)-1

        while l<=r:
            remain = limit - res[r]
            r -= 1
            ans += 1
            
            if l<=r and remain >= res[l]:
                l += 1

        return ans