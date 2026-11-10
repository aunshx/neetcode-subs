class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def compute(n):
            total = 0
            while n > 0:
                total += (n%10)**2
                n //= 10
            return total

        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = compute(n)

        return True