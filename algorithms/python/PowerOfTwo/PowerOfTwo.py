class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n&(n-1) == 0

# There is only one 1 in binary for the number which is power of 2
# 2: 10
# 4: 100
# 8: 1000
# 16: 10000
# So (n - 1) will be all 1s with one bit less, doing & between the two will give all 0s.


