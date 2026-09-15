class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minz = float('inf')
        profit = 0
        maxProfit = 0

        for x in prices:
            if x < minz:
                minz = x
            
            profit = x - minz

            if profit > maxProfit:
                maxProfit = profit
        return maxProfit
        
