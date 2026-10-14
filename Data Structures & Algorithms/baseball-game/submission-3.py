class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for val in operations:
            print(stack)
            if val == '+':
                if stack:
                    stack.append(stack[-1]+stack[-2])
            elif val == 'D':
                if stack:
                    stack.append(stack[-1]*2)
            elif val == 'C':
                if stack:
                    stack.pop()
            else:
                stack.append(int(val))

        return sum(stack)
                