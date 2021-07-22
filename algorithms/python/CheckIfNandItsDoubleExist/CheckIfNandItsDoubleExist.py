from typing import List

class Solution:
  def checkIfExist(self, arr: List[int]) -> bool:
    d = {}
    for i in range(len(arr)):
      if arr[i] in d:
        return True
      else:
        d[2*arr[i]] = arr[i]

    for i in range(len(arr)):
      if arr[i] in d and arr[i] != 0:
        return True
    return False

  # Using a Set, one pass iteration, check if the Set contains 2*i
  # or if i is even, and the Set contains i/2
  def checkIfExist2(self, arr: List[int]) -> bool:
    s = set()
    for i in arr:
      if 2*i in s or (i%2==0 and i/2 in s):
        return True
      else:
        s.add(i)
    return False

n = [7,1,14,11]
# True
n = [3,1,7,11]
# False
n = [0,0,0]
# true
print(Solution().checkIfExist(n))
