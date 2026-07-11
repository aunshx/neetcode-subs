class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits)-1, -1, -1):
            val = 0
            if i == len(digits) - 1:
                val = digits[i] + 1
            else:
                val = digits[i] + carry
            if val < 9:
                digits[i] = val
                return digits
            else:
                digits[i] = val%10
                carry = val//10
            
        return digits if carry != 1 else [1] + digits
        