class FreqStack:

    def __init__(self):
        self.count = {}
        self.freq = [[]]

    def push(self, val: int) -> None:
        self.count[val] = self.count.get(val, 0) + 1
        if len(self.freq) <= self.count[val]:
            self.freq.append([val])
        else:
            self.freq[self.count[val]].append(val) 

    def pop(self) -> int:
        val = self.freq[-1].pop()
        self.count[val] -= 1
        if self.count[val] == 0:
            del self.count[val]
        if len(self.freq[-1]) < 1:
            self.freq.pop()
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()