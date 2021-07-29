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
    var counts = Array(repeating: 0, count: 101)
    // count the number of occurrence of each height and store them in the array counts
    for height in heights {
      counts[height] += 1
    }

    // This height is actually the index of the counts array
    var height = 0
    var counter = 0
    for i in 0..<heights.count {
      // check if there is any height at this position in counts array
      // counts[height] is the number of occurrence of the height in the original heights array
      // if it is 0, meaning there is no occurrence at this position
      while counts[height] == 0 {
        height += 1
      }

      // heights[i] is the value(height) at the index i
      // remember height is the index of the counts array, it is also a value of the heights array
      // if this two does not match, we find one that is the wrong position.
      if heights[i] != height {
        counter += 1
      }
      // Then we decrease the number of occurrence of the height by 1 and continue the next comparision.
      // For example if height == 1, and counts[height] == 3 that means for the height 1,
      // it should appears 3 times in a consecutive order
      counts[height] -= 1
    }
    return counter
  }
}

assert(Solution().heightChecker([1,1,4,2,1,3]) == 3)
assert(Solution().heightChecker([5,1,2,3,4]) == 5)
assert(Solution().heightChecker([1,2,3,4,5]) == 0)

assert(Solution().heightChecker2([1,1,4,2,1,3]) == 3)
assert(Solution().heightChecker2([5,1,2,3,4]) == 5)
assert(Solution().heightChecker2([1,2,3,4,5]) == 0)

print("PASS")
