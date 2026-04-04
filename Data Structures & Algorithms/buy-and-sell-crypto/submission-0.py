class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        profit = 0
        
        for left in range(len(prices)):
            right = left + 1
            highest_right = 0
            while left < right and right < len(prices):
                highest_right = max(highest_right, prices[right])
                profit = max(profit, highest_right - prices[left])
                right += 1
        
        return profit



        
       



        