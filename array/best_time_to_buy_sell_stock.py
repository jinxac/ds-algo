
class Solution:
    def one_pass(self, prices):
        if not prices:
            return 0

        min_element = prices[0]
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < min_element:
                min_element = prices[i]
            else:
                max_profit = max(prices[i] - min_element, max_profit)

        return max_profit

    def maxProfit(self, prices: List[int]) -> int:
        return self.one_pass(prices)
