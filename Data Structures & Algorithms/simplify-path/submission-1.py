class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split('/')
        stack = []

        for s in arr:
            if s:
                if s == '..':
                    if stack:
                        stack.pop()
                else:
                    if s != '.':
                        stack.append(s)
                    
        return '/' + '/'.join(stack)
        