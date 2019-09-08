from typing import List

class Solution:
    # O(n)
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)

    # O(lgn)
    def searchInsert_binary_search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid+1
            else:
                high = mid-1
        return low

assert Solution().searchInsert([1,3,5,6], 5) == 2
assert Solution().searchInsert_binary_search([1,3,5,6], 2) == 1
assert Solution().searchInsert_binary_search([1,3,5,6], 7) == 4
assert Solution().searchInsert_binary_search([1,3,5,6], 0) == 0
assert Solution().searchInsert_binary_search([1,3], 2) == 1

print("OH YEAH!")
