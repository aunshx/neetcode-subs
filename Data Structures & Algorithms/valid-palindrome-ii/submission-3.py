class Solution:
    def isPalin(self, s:str, l:int, r:int) -> bool:
        while l<r:
            if s[l] != s[r]:
                return False 
            l += 1
            r -= 1
        return True 

    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1

        while l<r:
            if s[l] != s[r]:
                return self.isPalin(s, l+1,r) or self.isPalin(s, l,r-1)

            l += 1
            r -= 1

        return True