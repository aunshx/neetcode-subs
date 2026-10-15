from heapq import heappop, heappush

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.heap = []
        self.counter = 0
        self.m = {}
        self.last = {}

    def get(self, key: int) -> int:
        if key in self.m:
            self.counter += 1
            self.last[key] = self.counter
            heappush(self.heap, (self.counter, key))
            return self.m[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self.m[key] = value
        self.counter += 1
        self.last[key] = self.counter
        heappush(self.heap, (self.counter, key))
        while len(self.m) > self.capacity:
            t, oldKey = heappop(self.heap)
            if self.last[oldKey] == t:
                del self.last[oldKey]
                del self.m[oldKey]


