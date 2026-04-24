class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSoFar = float('inf')
        profit = 0
        for price in prices:
            minSoFar = min(minSoFar, price)
            profit = max(profit,price - minSoFar)
        
        return profit
            
        