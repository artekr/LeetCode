
# Recursive memorization
class Solution1:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n+1)
        return self.climbStairsMemo(n, memo)

    def climbStairsMemo(self, n: int, memo: [int]):
        if n == 1 or n == 2:
            return n
        if memo[n] == 0:
            memo[n] = self.climbStairsMemo(n-1, memo) + self.climbStairsMemo(n-2, memo)
        return memo[n]

# Bottom up Dynamic Programming
class Solution2:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        x, y = 1, 2
        for _ in range(2, n):
            subtotal = x + y
            x = y
            y = subtotal
        return y


print(Solution2().climbStairs(6))
# expected: 13

    
