from typing import List

# Naive
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        last = len(digits)-1
        if digits[last] < 9:
            digits[last] += 1
            return digits
        while last > 0 and digits[last] == 9:
            digits[last] = 0
            if digits[last - 1] != 9:
                digits[last - 1] += 1
                return digits
            last -= 1

        if digits[last] == 9:
            digits[last] = 1
            digits.append(0)
        else:
            digits[last] += 1
        return digits


print(Solution().plusOne([1,2,3]))
# expected: [1,2,4]

print(Solution().plusOne([1,2,9]))
# expected: [1,3,0]

print(Solution().plusOne([1,9,9]))
# expected: [2,0,0]

print(Solution().plusOne([9,9,9]))
# expected: [1,0,0,0]