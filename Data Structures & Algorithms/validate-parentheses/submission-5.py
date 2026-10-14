class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {
            ']': '[',
            '}': '{',
            ')': '('
        }

        for c in s:
            if c == '[' or c =='{' or c == '(':
                stack.append(c)
            else:
                if not stack:
                    return False
                val = stack.pop()
                if m[c] != val:
                    return False

        return len(stack) == 0