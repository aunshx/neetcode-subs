from heapq import heapify, heappop, heappush
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        waiting = deque()
        time = 0
        tasksCount = defaultdict(int)
        for t in tasks:
            tasksCount[t] += 1
        ready = [-count for count in tasksCount.values()]
        heapify(ready)

        while ready or waiting:
            time += 1
            if ready:
                copies_left = -heappop(ready) - 1
                if copies_left > 0:
                    waiting.append((copies_left, time+n))

            if waiting:
                copies_left, free_after = waiting[0]
                if free_after == time:
                    waiting.popleft()
                    heappush(ready, -copies_left)

        return time