class Solution:
    def reverseString(self, s: List[str]) -> None:
        l,r=0,len(s)-1

        while l<r:
            s[l],s[r] = s[r],s[l]
            r -= 1
            l += 1
        