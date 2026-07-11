import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        heap = []
        for n in nums:
            mp[n] = mp.get(n, 0) + 1

        for key,v in mp.items():
            heap.append([-v,key])

        heapq.heapify(heap)
        res = []
        while k > 0:
            print(k)
            v,key = heapq.heappop(heap)
            res.append(key)
            k -= 1

        return res



        
        