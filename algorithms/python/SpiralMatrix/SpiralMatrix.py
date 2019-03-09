from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix:
                matrix = self.rotateMatrix(matrix)
        return res

    def rotateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        res = []
        while n > 0:
            a = []
            for i in range(0,m):
                a.append(matrix[i][n-1])
            res.append(a)
            n -= 1
        return res
        
print(Solution().rotateMatrix([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]))

# expected: [[4, 8 ,12], [3, 7, 11], [2, 6, 10], [1, 5, 9]]

print(Solution().spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]))

# expected: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]