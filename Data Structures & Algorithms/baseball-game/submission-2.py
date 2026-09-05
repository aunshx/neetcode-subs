class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for val in operations:
            n = len(stack)
            if val == '+':
                if n > 1:
                    stack.append(stack[n-1] + stack[n-2])
            elif val == 'C':
                if stack:
                    stack.pop()
            elif val == 'D':
                if stack:
                    stack.append(stack[n-1] * 2)
            else:
                stack.append(int(val))
        return sum(stack)               
