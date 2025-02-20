class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        p = 0
        while r<len(prices):
            if prices[l]<prices[r]:
                diff = prices[r] - prices[l]
                p = max(p, diff)
            else:
                l = r
            r+=1
        return p