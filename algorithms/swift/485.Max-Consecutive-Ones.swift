/**
 * Question Link: https://leetcode.com/problems/max-consecutive-ones/
 *
 * Use two variables, one as the global result, another within the loop to dynamically calculate the counter
 * at the current index.
 *
 * Time Complexity: O(n), Space Complexity: O(1)
 */

class Solution {
  func findMaxConsecutiveOnes(_ nums: [Int]) -> Int {
    var result = 0
    var counter = 0
    for i in nums {
      if i == 1 {
        counter += 1
        result = max(result, counter)
      } else {
        counter = 0
      }
    }
    return result
  }
}
