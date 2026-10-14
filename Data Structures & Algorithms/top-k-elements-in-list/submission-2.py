from heapq import heappop, heappush

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        heap = []
        for val in nums:
            m[val] = m.get(val,0) + 1

        for num,v in m.items():
            heappush(heap, (v,num))
            if len(heap) > k:
                heappop(heap)
                
        return [num for (v,num) in heap]