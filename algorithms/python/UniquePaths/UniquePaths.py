# Brute force
class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)


# Reserve memorization:
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        # m is column, n is row
        memo = [[0 for i in range(m)] for i in range(n)]
        return self.findPaths(m, n, 0, 0, memo)

    def findPaths(self, m: int, n: int, r: int, c: int, memo: [[int]]):
        if r == n or c == m:
            return 0
        if r == n - 1 and c == m - 1:
            return 1

        if memo[r][c] == 0:
            memo[r][c] = self.findPaths(m, n, r + 1, c, memo) + self.findPaths(m, n, r, c + 1, memo)
        return memo[r][c]


# Dynamic programming:
class Solution3:
    def uniquePaths(self, m: int, n: int) -> int:
        # m is column, n is row
        memo = [[0 for i in range(m)] for i in range(n)]
        for i in range(m):
            memo[0][i] = 1
        for i in range(n):
            memo[i][0] = 1
        for i in range(1, n):
            for j in range(1, m):
                memo[i][j] = memo[i - 1][j] + memo[i][j - 1]
        return memo[n - 1][m - 1]


print(Solution1().uniquePaths(3, 2))
# # expected: 3

print(Solution2().uniquePaths(7, 3))
# expected: 28

print(Solution3().uniquePaths(23, 12))
# # expected: 193536720
