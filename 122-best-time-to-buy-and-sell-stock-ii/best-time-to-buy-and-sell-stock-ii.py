class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        for i in range(1, len(prices)):
            if prices[i]>prices[i-1]:
                p = p + (prices[i]-prices[i-1])
        return p