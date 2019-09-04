from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return 0
        begin = 0
        after = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                begin = i-1
                break
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                after = i
        return 0 if after == begin else after - begin + 1


assert Solution().findUnsortedSubarray([2,6,4,8,10,9,15]) == 5
assert Solution().findUnsortedSubarray([1,2,3,3,3]) == 0
assert Solution().findUnsortedSubarray([1,3,2,2,2]) == 4

print("OH YEAH!")