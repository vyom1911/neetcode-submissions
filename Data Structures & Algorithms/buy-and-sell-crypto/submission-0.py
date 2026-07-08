class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price_so_far = prices[0]
        max_profit = 0

        for price in prices[1:]:
            profit_today = price - min_price_so_far
            max_profit = max(max_profit, profit_today)
            min_price_so_far = min(min_price_so_far,price)
        
        return max_profit
