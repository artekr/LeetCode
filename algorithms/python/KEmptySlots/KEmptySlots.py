from typing import List


class Solution:
    def kEmptySlots(self, flowers: List[int], k: int) -> int:
        if k >= len(flowers):
            return -1
        # To create a days array is a bit tricky sine, Leetcode will give Time Exceed limit error
        # if not pre allocate the array size
        days = [0 for _ in range(len(flowers))]
        for i in range(0, len(flowers)):
            days[flowers[i] - 1] = i + 1

        left = 0
        right = k + 1
        res = float('inf')
        for i in range(1, len(days)):
            if right < len(days):
                if days[i] > days[left] and days[i] > days[right]:
                    continue
                if i == right:
                    res = min(res, max(days[left], days[right]))
                left = i
                right = k + 1 + i
        return -1 if (res == float('inf')) else res

print(Solution().kEmptySlots([1, 6, 3, 2, 4, 5], 2))
# expected: 3

print(Solution().kEmptySlots([2, 1, 4, 5, 3], 2))
# expected: -1

print(Solution().kEmptySlots([2, 1, 4, 5, 3], 1))
# expected: 3

print(Solution().kEmptySlots([6, 5, 8, 9, 7, 1, 10, 2, 3, 4], 2))
# expected: 8

print(Solution().kEmptySlots([1, 3, 2], 1))
# expected: 2

print(Solution().kEmptySlots([3, 9, 2, 8, 1, 6, 10, 5, 4, 7], 1))
# expected: 6
