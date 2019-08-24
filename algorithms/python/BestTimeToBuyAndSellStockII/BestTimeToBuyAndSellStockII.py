from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                maxProfit += prices[i] - prices[i-1]
        return maxProfit

########
# Test #
########

a = [7,1,5,3,6,4]
print(Solution().maxProfit(a))
# expected: 7

a = [7,6,5,4,3,1]
print(Solution().maxProfit(a))
# expected: 0