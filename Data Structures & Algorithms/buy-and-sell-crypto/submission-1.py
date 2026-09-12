class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        i,j=0,1
        n = len(prices)

        while j < n:
            if prices[j] > prices[i]:
                diff = prices[j] - prices[i]
                maxP = max(maxP,diff)
            else:
                i = j
            j += 1
            
        return maxP 
