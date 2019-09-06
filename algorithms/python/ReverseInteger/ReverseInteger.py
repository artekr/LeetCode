class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2 ** 31
        MIN = -1 * MAX
        if x > MAX or x < MIN:
            return 0
        sign = 1
        rev = 0
        if x < 0:
            sign = -1
            x *= sign
        while x != 0:
            d = x % 10
            x = int(x/10)
            rev = rev*10 + d
        return 0 if rev>MAX or rev<MIN else rev*sign

assert Solution().reverse(123) == 321
assert Solution().reverse(-123) == -321
assert Solution().reverse(120) == 21
assert Solution().reverse(1534236469) == 0

print("OH YEAH!")
