class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mp = {
            1: "",
            2: "abc",
            3: "def",
            4: 'ghi',
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
            0: "+"
        }


        res = []
        def backtrack(i,path):
            if len(path) == len(digits):
                res.append(''.join(path[:]))
                return 


            for ch in mp[int(digits[i])]:
                path.append(ch)
                backtrack(i+1, path)
                path.pop()
                
        if digits:
            backtrack(0,[])

        return res