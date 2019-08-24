class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == 0:
            return num
        n = int(num)
        if n == 0:
            return '0'





a = Solution().removeKdigits("123", 1)
# print(a)

