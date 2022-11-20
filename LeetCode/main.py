from typing import List

prices = [3, 2, 6, 5, 0, 3]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minvalue = prices[0]
        maxvalue = prices[0]
        minvalueindex = 0
        maxvalueindex = 0
        out = 0

        for i, v in enumerate(prices):
            if minvalue > v and i != len(prices) - 1:
                minvalue = v
                minvalueindex = i

            if maxvalue < v:
                maxvalue = v
                maxvalueindex = i

            if maxvalueindex < minvalueindex:
                maxvalue = v
                maxvalueindex = i

            if out < maxvalue - minvalue:
                out = maxvalue - minvalue

        return out


profit = Solution()
print(profit.maxProfit(prices))
