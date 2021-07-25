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

assert(Solution().checkIfExist([7,1,14,11]) == true)
assert(Solution().checkIfExist([3,1,7,11]) == false)
assert(Solution().checkIfExist([0,0,0]) == true)

print("PASS")
