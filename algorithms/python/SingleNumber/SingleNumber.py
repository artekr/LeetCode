from typing import List

class Solution:
    def singleNumber_hashtable1(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        for k in d.keys():
            if d[k] == 1:
                return k

    def singleNumber_hashtable2(self, nums: List[int]) -> int:
        hash_table = {}
        for n in nums:
            try:
                hash_table.pop(n)
            except:
                hash_table[n] = 1
        # popitem() will pop the only the single item (value, 1)
        return hash_table.popitem()[0]

    def singleNumber_math(self, nums: List[int]) -> int:
        # 2∗(a+b+c)−(a+a+b+b+c)=c
        return 2*sum(set(nums)) - sum(nums)

    def singleNumber_bitManipulation(self, nums: List[int]) -> int:
        """
            If we take XOR of zero and some bit, it will return that bit
                a⊕0=a
            If we take XOR of two same bits, it will return 0
                a⊕a=0
                a⊕b⊕a=(a⊕a)⊕b=0⊕b=b
            So we can XOR all bits together to find the unique number.
        """
        a = 0
        for n in nums:
            a ^= n
        return a

assert Solution().singleNumber_hashtable1([2,2,1]) == 1
assert Solution().singleNumber_hashtable2([1,2,2,1,4]) == 4
assert Solution().singleNumber_math([1,2,2,1,4]) == 4
assert Solution().singleNumber_bitManipulation([1,2,1,2,3]) == 3