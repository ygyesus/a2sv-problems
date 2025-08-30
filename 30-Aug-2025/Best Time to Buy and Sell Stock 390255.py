# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        MIN = prices[0]
        for i in range(1, len(prices)):
            diff = prices[i] - MIN
            profit = max(profit, diff)
            MIN = min(MIN, prices[i])

        return profit