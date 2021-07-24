/**
 * Question Link: https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
 * Starts from the end to start, keep the current max
 * Time Complexity: O(n), Space Complexity: O(n)
 */

class Solution {
  func replaceElements(_ arr: [Int]) -> [Int] {
    guard arr.count != 1 else { return [-1] }

    var cur_max = -1
    var result = [Int](repeating: -1, count: arr.count)

    var i = result.count - 2
    var j = result.count - 1
    while i >= 0 {
      cur_max = max(cur_max, arr[j])
      result[i] = cur_max
      i -= 1
      j -= 1
    }
    return result
  }
}

let n = [17,18,5,4,6,1]
// let n = [400,1]
print(Solution().replaceElements(n))
