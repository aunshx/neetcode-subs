class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        store = set(('+','-','/','*'))

        for t in tokens:
            if t not in store:
                stack.append(int(t))
            else:
                if stack:
                    v1 = stack.pop()
                    v2 = stack.pop()
                if t == '+':
                    stack.append(v1 + v2)
                elif t == '*':
                    stack.append(v1 * v2)
                elif t == '/':
                    stack.append(int(v2 / v1))
                else:
                    stack.append(v2 - v1)
        return stack[0]

