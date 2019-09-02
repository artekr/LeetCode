from typing import List

class Solution:
    # space complexity: O(n)
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        helper = [0] * len(nums)
        for n in nums:
            helper[n-1] = n
        for i in range(len(helper)):
            if helper[i] == 0:
                result.append(i+1)
        return result
    
    # space complexity: O(1)
    def findDisappearedNumbers_optimal(self, nums: List[int]) -> List[int]:
        result = []

        # iterate the array, use the element value as the index of the array and mark that element as negative
        for i in range(len(nums)):
            current = abs(nums[i])-1
            nums[current] = -abs(nums[current])

        # The non-negative elements' index means the missing value
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i+1)
        return result

assert Solution().findDisappearedNumbers([1,1,2,2,1]) == [3,4,5]
assert Solution().findDisappearedNumbers_optimal([4,3,2,7,8,2,3,1]) == [5,6]

print("Oh YEAH!")
