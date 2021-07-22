/**
 * Question Link: https://leetcode.com/problems/check-if-n-and-its-double-exist/
 * Time Complexity: O(n), Space Complexity: O(n)
 */

class Solution {
  func checkIfExist(_ arr: [Int]) -> Bool {
    var s = Set<Int>()
    for i in arr {
      if s.contains(2*i) || (i%2 == 0 && s.contains(i/2)) {
        return true
      } else {
        s.insert(i)
      }
    }
    return false
  }
}

// let n = [7,1,14,11]
// let n = [3,1,7,11]
let n = [0,0,0]
print(Solution().checkIfExist(n))
