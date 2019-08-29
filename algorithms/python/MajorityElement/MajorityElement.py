from typing import List

class Solution:
    def majorityElement_hashtable(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        
        for k in d.keys():
            if d[k] > len(nums)/2:
                return k

assert Solution().majorityElement_hashtable([2,2,1,1,1,2,2]) == 2