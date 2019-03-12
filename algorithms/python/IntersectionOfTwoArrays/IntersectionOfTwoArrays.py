from typing import List
class Solution1:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        t1 = {}
        t2 = {}
        for num in nums1:
            if num not in t1.keys():
                t1[num] = num
        for num in nums2:
            if num not in t2.keys():
                t2[num] = num
        res = []
        for k in t1.keys():
            if k in t2.keys():
                res.append(k)
        return res

class Solution2:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        if len(set1) < len(set2):
            return [x for x in set1 if x in set2]
        else:
            return [x for x in set2 if x in set1]

print(Solution1().intersection([1,2,2,1], [2,2]))
# expected: [2]

print(Solution2().intersection([4,9,5],[9,4,9,8,4]))
# expected: [9,4] or [4,9]