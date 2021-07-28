//: 1051 Height Checker
/**
 * Question Link: https://leetcode.com/problems/height-checker/
 */

class Solution {
  /// Sorte the array and compare the two
  /// Time Complexity: O(nlogn), Space Complexity: O(n)
  func heightChecker(_ heights: [Int]) -> Int {
    let expected = heights.sorted()
    var counter = 0
    for i in 0..<heights.count {
      if heights[i] != expected[i] {
        counter += 1
      }
    }
    return counter
  }

  /// Counting sort
  /// Time Complexity: O(n), Space Complexity: O(n)
  func heightChecker2(_ heights: [Int]) -> Int {
    var counter = 0
    // TODO
    return counter
  }
}

assert(Solution().heightChecker([1,1,4,2,1,3]) == 3)
assert(Solution().heightChecker([5,1,2,3,4]) == 5)
assert(Solution().heightChecker([1,2,3,4,5]) == 0)

// assert(Solution().heightChecker2([1,1,4,2,1,3]) == 3)
// assert(Solution().heightChecker2([5,1,2,3,4]) == 5)
// assert(Solution().heightChecker2([1,2,3,4,5]) == 0)

print("PASS")
