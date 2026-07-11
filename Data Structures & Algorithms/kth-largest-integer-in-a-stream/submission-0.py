import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums[:]
        self.limit = k
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.limit:
            heapq.heappop(self.heap)
        return self.heap[0]
