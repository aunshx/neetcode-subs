from heapq import heappop, heappush

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for val in nums:
            heappush(heap, val)
            if len(heap) > k:
                heappop(heap)

        return heap[0]