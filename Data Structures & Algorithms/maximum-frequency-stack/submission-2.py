from heapq import heappop, heappush

class FreqStack:

    def __init__(self):
        self.m = {}
        self.heap = []
        self.t = 0

    def push(self, val: int) -> None:
        self.m[val] = self.m.get(val,0) + 1
        self.t += 1
        heappush(self.heap, (-self.m[val], -self.t, val))

    def pop(self) -> int:
        _,_,val = heappop(self.heap)
        self.m[val] = self.m[val]-1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()