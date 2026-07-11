class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        self.stack.append(price)
        days = 0
        for i in range(len(self.stack)-1,-1,-1):
            if self.stack[i] <= price:
                days += 1
            else:
                break
        return days


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)