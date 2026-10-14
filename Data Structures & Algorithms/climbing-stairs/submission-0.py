class Solution:
    def climbStairs(self, n: int) -> int:
        m = {}
        def climb(n):
            if n <= 1:
                return 1
            if n in m:
                return m[n]
            m[n] = climb(n-1) + climb(n-2)
            return m[n]

        return climb(n)