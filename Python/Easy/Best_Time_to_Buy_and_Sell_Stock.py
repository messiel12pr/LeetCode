'''

    121. Best Time to Buy and Sell Stock

    Solution

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_profit = 0

        while r < len(prices):
            if  prices[r] - prices[l] > max_profit:
                max_profit = prices[r] - prices[l]
            
            if prices[l] > prices[r]:
                l = r
                r += 1
            
            else:
                r += 1

        return max_profit
