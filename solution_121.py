from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = []
        Max = 0
        for r in prices:
            if not profit:
                profit.append(r)
            elif profit[0] > r:
                while (profit) and (profit[0] > r):
                    profit.pop(0)
                profit.append(r)
            elif profit[0] <= r:
                Max = max(Max, r-profit[0])
                profit.append(r)
        return Max
