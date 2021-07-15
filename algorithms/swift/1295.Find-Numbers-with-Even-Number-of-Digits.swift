/**
 * Question Link: https://leetcode.com/problems/max-consecutive-ones/
 * Time Complexity: O(n), Space Complexity: O(1)
 */

class Solution1 {
  func findNumbers(_ nums: [Int]) -> Int {
    var result = 0
    for i in nums {
      let s = String(i)
      if s.count % 2 == 0 {
        result += 1
      }
    }
    return result
  }
}

/**
 * Manually count the number of digits of the Int by dividing by 10.
 */
class Solution2 {
  func findNumbers(_ nums: [Int]) -> Int {
    var result = 0
    for i in nums {
      var count = 0
      var x = i
      while (x > 0) {
        count += 1
        x /= 10
      }
      if count % 2 == 0 {
        result += 1
      }
    }
    return result
  }
}
