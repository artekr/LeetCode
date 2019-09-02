from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1

        # Print Result
        for n in nums:
            print(n, end = " ")
        print()


    def moveZeroes_2(self, nums: List[int]) -> None:
        lastNoneZeroPosition = 0
        # Move all the none zero elements to the front of the array
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNoneZeroPosition] = nums[i]
                lastNoneZeroPosition += 1

        # Fill the rest elements of the array with zeros
        for i in range(lastNoneZeroPosition, len(nums)):
            nums[i] = 0

        # Print Result
        for n in nums:
            print(n, end = " ")
        print()


Solution().moveZeroes_2([0,1,0,3,12])
# expected: 1 3 12 0 0

Solution().moveZeroes([2,1])
# expected: 2 1