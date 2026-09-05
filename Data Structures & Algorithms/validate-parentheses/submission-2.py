class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        setting = {
            '}':'{',
            ']':'[',
            ')':'('
        }

        for val in s:
            if val in setting:
                if stack:
                    curr = stack.pop() 
                    if curr != setting[val]:
                        return False
                else:
                    return False
            else:
                stack.append(val)
        return len(stack) == 0