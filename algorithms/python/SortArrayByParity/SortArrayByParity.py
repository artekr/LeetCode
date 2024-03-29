from typing import List

class Solution:
  # In place, two pointers
  # Time Complexity: O(n), Space Complexity: O(1)
  def sortArrayByParity(self, nums: List[int]) -> List[int]:
    i = 0
    j = len(nums) - 1
    while i < j:
      if nums[i] % 2 == 1 and nums[j] % 2 == 0:
        nums[i], nums[j] = nums[j], nums[i]

      if nums[i] % 2 == 0:
        i+=1
      if nums[j] % 2 == 1:
        j-=1
    return nums

assert Solution().sortArrayByParity([3,1,2,4]) == [4,2,1,3]
assert Solution().sortArrayByParity([3]) == [3]
assert Solution().sortArrayByParity([3,4,1,2,5,7,8,10]) == [10, 4, 8, 2, 5, 7, 1, 3]

print("PASS")
