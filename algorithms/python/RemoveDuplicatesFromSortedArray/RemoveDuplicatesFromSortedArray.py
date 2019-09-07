from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        pos = 0
        counter = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[pos]:
                pos = i
                counter += 1
        return counter

        ##
        ## Because the problem requires to modify the array
        ##
        # if len(nums) < 2:
        #     return len(nums)
        # pos = 0
        # for i in range(1, len(nums)):
        #     if nums[i] != nums[pos]:
        #         pos += 1
        #         nums[pos] = nums[i]
        # return pos + 1
        
assert Solution().removeDuplicates([0,0,0,0,0]) == 1
assert Solution().removeDuplicates([1,1,2]) == 2
assert Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5

print("OH YEAH!")