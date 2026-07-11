class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five,ten = 0,0

        for n in bills:
            if n == 5:
                five += 1
            elif n == 10:
                five,ten = five-1, ten+1
            elif ten > 0:
                five, ten = five - 1, ten - 1
            else:
                five -= 3

            if five < 0:
                return False

        return True