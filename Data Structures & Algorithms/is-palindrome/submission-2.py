class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.strip()

        l,r=0,len(s)-1

        while l<r:
            isLeftCorrect = s[l].isalnum()
            isRigthCorrect = s[r].isalnum()
            
            if isLeftCorrect and isRigthCorrect:
                if s[l].lower() != s[r].lower():
                    return False 
                l +=1
                r -= 1
            else:
                if not isLeftCorrect:
                    l += 1
                if not isRigthCorrect:
                    r -= 1
        return True

