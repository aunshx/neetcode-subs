
from heapq import heappop, heappush, heapify
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []

        for val in nums:
            heappush(self.heap, val)
            if len(self.heap) > self.k:
                heappop(self.heap)

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        if len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]
