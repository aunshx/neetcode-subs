class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            maxProfit = max(maxProfit, prices[i]-curr)
            curr = min(curr, prices[i])

        return maxProfit