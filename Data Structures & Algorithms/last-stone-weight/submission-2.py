from heapq import heapify, heapify_max, heappop, heappush

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapify(heap)

        while len(heap) > 1:
            val1 = -heappop(heap)
            val2 = -heappop(heap)
            if val1 != val2:
                heappush(heap, -(val1-val2))

        return -heap[0] if heap else 0