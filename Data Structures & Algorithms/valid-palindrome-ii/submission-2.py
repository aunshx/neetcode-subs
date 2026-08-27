class Solution:
    def isPal(self, l, r, s) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True 

    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<r:
            if s[l] != s[r]: 
                return self.isPal(l+1,r,s) or self.isPal(l,r-1,s)
            l += 1
            r -= 1
        return True
            