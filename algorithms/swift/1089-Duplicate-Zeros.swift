/**
 * Question Link: https://leetcode.com/problems/duplicate-zeros/
 *
 */

class Solution {
  // Time Complexity: O(n^2), Space Complexity: O(1)
  func duplicateZeros1(_ arr: inout [Int]) {
    var i = 0
    while i < arr.count {
      if arr[i] == 0 {
        // approach 1
        var j = arr.count - 1
        while j > i {
          arr[j] = arr[j-1]
          j -= 1
        }
        /// There are other ways provided by swift to do a backward iteration.
        /// However, it will be more time consuming since the operation itself takes time
        /// approach 2
        ///    for j in stride(from: arr.count-1, to: i, by: -1) {
        ///      arr[j] = arr[j-1]
        ///    }
        ///
        /// approach 3
        ///    for j in (i+1..<arr.count).reversed() {
        ///      arr[j] = arr[j-1]
        ///    }
        i += 1
      }
      i += 1
    }
  }

  // Time Complexity: O(n), Space Complexity: O(n)
  func duplicateZeros2(_ arr: inout [Int]) {
    var i = 0
    var j = 0
    var result = Array(repeating: -1, count: arr.count)
    while j < arr.count {
      if arr[i] != 0 {
        result[j] = arr[i]
      } else {
        result[j] = 0
        if j+1 == arr.count {
          break
        } else {
          result[j+1] = 0
        }
        j += 1
      }
      i += 1
      j += 1
    }
    arr = result
  }

  // Time Complexity: O(n), Space Complexity: O(1)
  func duplicateZeros3(_ arr: inout [Int]) {
    var zeroCount = 0
    // count the number of zeros
    for n in arr {
      if n == 0 {
        zeroCount += 1
      }
    }

    var i = arr.count - 1
    var j = i + zeroCount
    // j is currently out of bound, so we need to check
    // if j is in bound each time in the loop before we make the copy
    while i >= 0 {
      if arr[i] != 0 {
        if j < arr.count {
          arr[j] = arr[i]
        }
      } else {
        if j < arr.count {
          arr[j] = arr[i]
        }
        // if it is zero, we decrease j, and make a copy one more time
        j -= 1
        if j < arr.count {
          arr[j] = arr[i]
        }
      }
      i -= 1
      j -= 1
    }
  }
}
