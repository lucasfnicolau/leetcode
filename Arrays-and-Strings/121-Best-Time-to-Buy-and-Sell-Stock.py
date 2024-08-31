# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1374141239

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = (0,prices[0])
        maxProfit = 0

        for i in range(1, len(prices)):
            if prices[i] <= lowest[1]:
                lowest = (i, prices[i])
        
            profit = 0 if i <= lowest[0] else prices[i] - lowest[1]
            maxProfit = profit if profit > maxProfit else maxProfit

        return maxProfit