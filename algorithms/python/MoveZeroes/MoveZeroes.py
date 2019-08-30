from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return
        p = 0
        n = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                n += 1
            else:
                if nums[p] != 0:
                    p += 1
                    n += 1
                else:
                    tmp = nums[p]
                    nums[p] = nums[i]
                    nums[i] = tmp
                    p = n

        for n in nums:
            print(n, end = " ")
        print()

Solution().moveZeroes([0,1,0,3,12])
# expected: 1 3 12 0 0

Solution().moveZeroes([2,1])
# expected: 2 1