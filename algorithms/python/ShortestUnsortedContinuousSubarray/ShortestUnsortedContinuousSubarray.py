from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if not nums or len(nums) == 1:
            return 0
        begin = 0
        after = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                begin = i-1
                break
        print(begin)
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                after = i
        return after - begin + 1

a = [2,6,4,8,10,9,15]

l = Solution().findUnsortedSubarray(a)
print(l)