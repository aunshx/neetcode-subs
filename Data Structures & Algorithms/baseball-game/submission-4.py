class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack, res = [], 0

        for val in operations:
            if val == '+':
                if stack:
                    total = stack[-1]+stack[-2]
                    res += total
                    stack.append(total)
            elif val == 'D':
                if stack:
                    total = stack[-1]*2
                    res += total
                    stack.append(total)
            elif val == 'C':
                if stack:
                    res -= stack.pop()
            else:
                res += int(val)
                stack.append(int(val))

        return res
                