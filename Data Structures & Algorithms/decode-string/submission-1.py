class Solution:
    def decodeString(self, s: str) -> str:
        str_stack = []
        count_stack = []
        curr_substr = ""
        i = 0
        k = 0
        while i < len(s):
            if s[i].isdigit():
                k = k * 10 + int(s[i])
            elif s[i] == '[':
                str_stack.append(curr_substr)
                count_stack.append(k)
                curr_substr = ""
                k = 0
            elif s[i] == ']':
                temp = curr_substr
                curr_substr = str_stack.pop()
                count = count_stack.pop()
                curr_substr += temp * count
            else:
                curr_substr += s[i]
                
            i += 1

        return curr_substr
                