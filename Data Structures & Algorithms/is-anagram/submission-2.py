class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        arr = [0] * 26

        for s_char, t_char in zip(s,t):
            arr[ord(s_char)-ord('a')] += 1
            arr[ord(t_char)-ord('a')] -= 1

        return all(v == 0 for v in arr)

        