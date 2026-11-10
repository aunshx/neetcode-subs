class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        total = 1
        res = []
        for i in range(len(digits)-1,-1,-1):
            total += carry + digits[i]
            if total > 9:
                carry = 1
                total %= 10
                res.append(total)
            else:
                res.append(total)
                total = 0
                carry = 0

        if carry == 1:
            res.append(1)

        res.reverse()
        return res