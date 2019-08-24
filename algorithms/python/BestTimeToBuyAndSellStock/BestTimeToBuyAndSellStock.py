from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buy = prices[0] if prices else 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                buy = min(buy, prices[i-1])
                maxProfit = max(maxProfit, prices[i] - buy)
        return maxProfit

########
# Test #
########

a = [7,1,5,3,6,4]
print(Solution().maxProfit(a))
# expected: 5

a = [7,6,5,4,3,1]
print(Solution().maxProfit(a))
# expected: 0

a = [2,1,2,1,0,1,2]
print(Solution().maxProfit(a))
# expected: 0
