class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = [a.lower() for a in s if a.isalnum()]
        l,r=0,len(clean)-1

        while l<r:
            if clean[l] != clean[r]:
                return False
            l += 1
            r -= 1

        return True