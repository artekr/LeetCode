# Using bit manipulation

# Rules:
# For lives(1)
# < 2    : 0
# = 2, 3 : 1
# > 3    : 0

# For deads(0)
# = 3    : 1

# Add the updated value in a higher bit, and the lower bit represent the current state

# current 0 -> updated 0 = 00
# current 0 -> updated 1 = 10
# current 1 -> updated 0 = 01
# current 1 -> updated 1 = 11

# value & 1 = current state

from typing import List
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        # First iteration is to update the cell in entire matrix to two bits
        for i in range(0, m):
            for j in range(0, n):
                count = 0
                indices = [(i-1,j-1), (i,j-1), (i+1,j-1), (i-1,j), (i+1,j), (i-1,j+1), (i,j+1), (i+1,j+1)]
                # check neighbours
                for r, c in indices:
                    if 0 <= r < m and 0 <= c < n:
                        # check if live
                        if board[r][c] & 1:
                            count += 1
                # based on the count of its neighbours
                if board[i][j] == 1:
                    # Rule for lives(1)
                    if count < 2 or count > 3:
                        # Updated value will be 0, bits become 01, so do nothing here
                        continue
                    else:
                        # Updated value will be live(1), bits become 11, perform a _ior_ with 2 (10)
                        #    01
                        # |= 10
                        #-------
                        #    11
                        board[i][j] |= 2
                else:
                    # Rule for deads(0)
                    if count == 3:
                        # Updated value will be live(1), bits become 10, perform a _ior_ with 2 (10)
                        #    00
                        # |= 10
                        #-------
                        #    10
                        board[i][j] |= 2

        # Second iteration is to shift the bit in each cell to get the updated matrix
        for i in range(0, m):
            for j in range(0, n):
                board[i][j] = board[i][j] >> 1

a = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Solution().gameOfLife(a)
print(a)
# expected:
# [
#   [0, 0, 0],
#   [1, 0, 1],
#   [0, 1, 1],
#   [0, 1, 0]
# ]