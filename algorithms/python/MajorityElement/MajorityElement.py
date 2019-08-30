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

    def majorityElement_Boyer_Moore(self, nums: List[int]) -> int:
        candidate = None
        counter = 0

        for n in nums:
            if counter == 0:
                candidate = n
            counter += 1 if n == candidate else -1

        return candidate


assert Solution().majorityElement_hashtable([2,2,1,1,1,2,2]) == 2
assert Solution().majorityElement_Boyer_Moore([2,2,1,1,1,1,2]) == 1

print("OH, YEAH!")