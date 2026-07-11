import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            heap.append([math.sqrt(p[0]**2 + p[1]**2), p[0], p[1]])

        heapq.heapify(heap)

        res = []
        while k > 0:
            dist, x, y = heapq.heappop(heap)
            res.append([x,y])
            k -= 1

        return res
        