class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        profit = 0
        for right in range(len(prices)):
            profit = max(profit, prices[right] - prices[left])
            if prices[left] > prices[right]:
                left=right
        return profit


        