class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == 0:
            return num
        if int(num) == 0 or len(num) == k:
            return '0'
        result = []
        for n in num:
            while k > 0 and result and result[-1] > n:
                result.pop()
                k -= 1
            result.append(n)
        # After we went through the whole num string, if k stil greater than 0,
        # meaning we still need to remove k more digits from the stack
        # Since our stack already ordered, we just need to remove last k digits from the stack
        if k > 0:
            result = result[:-k]
        return ''.join(result).lstrip('0') or '0'


a = Solution().removeKdigits("1432219", 3)
print(a)
# expected: '1219'

a = Solution().removeKdigits("10200", 1)
print(a)
# expected: '200'

a = Solution().removeKdigits("1234506789", 9)
print(a)
# expected: '0'
