class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        else:
            peak = prices[0]
            valley = prices[0]
            profit = 0
            for number in prices:
                if number > peak:
                    peak = number
                else:
                    profit += peak - valley
                    peak = valley = number
            profit += peak - valley
            return profit
