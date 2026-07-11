class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(path, openBracket, close):
            if len(path) == n*2:
                res.append(''.join(path[:]))
                return 

            if openBracket < n:
                path.append('(')
                backtrack(path,openBracket+1,close)
                path.pop()
            
            if close < openBracket:
                path.append(')')
                backtrack(path,openBracket,close+1)
                path.pop()

        backtrack([],0,0)
        return res