class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 1
        total = 0
        while i < len(prices):
            if prices[i-1] < prices[i]:
                total += prices[i] - prices[i-1]
            i += 1
        return total