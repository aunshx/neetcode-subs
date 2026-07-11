class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(index, curr):
            if index > n:
                if len(curr) == k:
                    res.append(curr[:])
                return


            curr.append(index)
            backtrack(index+1, curr)
            curr.pop()
            backtrack(index+1, curr)

        backtrack(1,[])
        return res