class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        if k > len(arr):
            return -1
        total = 0
        for i in range(k):
            total += arr[i]
        res = []
        if threshold <= total // k:
            res.append(arr[:k])

        for i in range(k,n):
            total -= arr[i-k]
            total += arr[i]
            if threshold <= total // k:
                res.append(arr[i-k:i])
        
        return len(res)