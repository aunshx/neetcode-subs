from heapq import heappop, heappush

class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heappush(self.maxHeap, -num)
        val = -heappop(self.maxHeap)
        heappush(self.minHeap, val)
        if len(self.minHeap) > len(self.maxHeap):
            val = heappop(self.minHeap)
            heappush(self.maxHeap, -val)

    def findMedian(self) -> float:
        if (len(self.minHeap) + len(self.maxHeap) )% 2 == 0:
            return (self.minHeap[0] + -self.maxHeap[0])/2
        return -self.maxHeap[0]
        