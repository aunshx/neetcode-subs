class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        i = len(s)-1
    
        while i >= 0:
            if i != len(s)-1 and m[s[i]] < m[s[i+1]]:
                total -= m[s[i]]
            else:
                total += m[s[i]]
            i -= 1

        return total
