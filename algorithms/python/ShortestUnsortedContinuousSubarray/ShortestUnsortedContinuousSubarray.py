from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return 0
        left = 0
        right = 0
        for i in range(1, len(nums)):
            if nums[i] >= nums[i-1]:
                left += 1
            else:
                break
        for i in range(left, len(nums)):
            if nums[i] <= nums[i-1]:
                right = i
        return 0 if right < left else right - left + 1


assert Solution().findUnsortedSubarray([2,6,4,8,10,9,15]) == 5
assert Solution().findUnsortedSubarray([1,2,3,3,3]) == 0
assert Solution().findUnsortedSubarray([1,3,2,2,2]) == 4
assert Solution().findUnsortedSubarray([1,2,3,4]) == 0
assert Solution().findUnsortedSubarray([1,3,2,3,3]) == 2

print("OH YEAH!")