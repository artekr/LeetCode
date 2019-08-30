from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l = len(nums)
        if l == 1:
            return nums[0]
        pre_max = nums[0]
        cur_max = nums[0] if nums[0] > nums[1] else nums[1]
        for i in range(2,l):
            pre_max = max(pre_max, nums[i-2])
            nums[i] = nums[i] + pre_max
            cur_max = max(cur_max, nums[i])
        return cur_max

assert Solution().rob([1,3,1]) == 3
assert Solution().rob([2,1,1,2]) == 4
assert Solution().rob([2,7,9,3,1]) == 12

print("Oh YEAH!")