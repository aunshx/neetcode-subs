from heapq import heappush, heappop

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []
        for i in range(k):
            heappush(heap,(-nums[i],i))

        res.append(-heap[0][0])

        l=1
        r=k
        while r<len(nums):
            heappush(heap, (-nums[r],r))
            while heap[0][1] < l:
                heappop(heap)
            res.append(-heap[0][0])
            r += 1
            l += 1

        return res