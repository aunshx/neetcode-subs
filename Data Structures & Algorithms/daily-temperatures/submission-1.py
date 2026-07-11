class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        res = [0]*n

        for i in range(n):
            while stack and stack[-1][0] < temperatures[i]:
                val, index = stack.pop()
                res[index] = i - index

            stack.append([temperatures[i],i])

        return res