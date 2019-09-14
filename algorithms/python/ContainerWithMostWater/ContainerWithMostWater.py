from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        s = 0
        e = len(height) - 1
        while s < e:
            if height[s] < height[e]:
                current = height[s]*(e-s)
                s += 1
            else:
                current = height[e]*(e-s)
                e -= 1
            maxArea = max(maxArea, current)
        return maxArea


assert Solution().maxArea([1,2,3]) == 2
assert Solution().maxArea([1,2,1]) == 2
assert Solution().maxArea([1,8,6,2,5,4,8,3,7]) == 49

print("OH YEAH!")
# using two pointers