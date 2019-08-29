from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        x = 0
        y = 0
        for i in range(0,len(nums)):
            if i % 2 == 0:
                x += nums[i]
            elif i % 2 == 1:
                y += nums[i]
        return max(x, y)


assert Solution().rob([1,2,3,1]) == 4

print("Oh YEAH!")