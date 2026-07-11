class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        e=1
        total = 0
        while e < len(prices):
            if prices[e-1] < prices[e]:
                total += (prices[e] - prices[e-1])
            e += 1

        return total