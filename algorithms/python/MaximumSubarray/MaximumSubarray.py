from typing import List

class Solution_dp:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0] if nums else 0
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i-1] + nums[i])
            result = max(result, nums[i])
        return result

########
# Test #
########

a = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution_dp().maxSubArray(a))
# expect: 6
# [4,-1,2,1]

a = [2,-1,2]
print(Solution_dp().maxSubArray(a))
# expect: 3
# [2,-1,2]