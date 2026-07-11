import heapq
import math
class Solution:



    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-n for n in gifts]
        heapq.heapify(heap)
        while k > 0:
            val = -heapq.heappop(heap)
            print(val, -math.isqrt(val))
            heapq.heappush(heap,-math.isqrt(val))
            k -= 1
        
        return -sum(heap)

        