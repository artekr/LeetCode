/**
 * Question Link: https://leetcode.com/problems/squares-of-a-sorted-array/
 * Time Complexity: O(n), Space Complexity: O(1)
 */

class Solution {
  func sortedSquares(_ nums: [Int]) -> [Int] {
    var result = Array(repeating: 0, count: nums.count)
    var i = 0
    var j = nums.count - 1
    var k = j
    while i <= j {
      if abs(nums[i]) > abs(nums[j]) {
        result[k] = nums[i] * nums[i]
        i += 1
      } else {
        result[k] = nums[j] * nums[j]
        j -= 1
      }
      k -= 1
    }
    return result
  }
}

// Append and reverse the result, reversed() will take O(n)
class Solution2 {
  func sortedSquares(_ nums: [Int]) -> [Int] {
    var result = [Int]()
    var i = 0
    var j = nums.count - 1
    while i <= j {
      if abs(nums[i]) > abs(nums[j]) {
        result.append(nums[i] * nums[i])
        i += 1
      } else {
        result.append(nums[j] * nums[j])
        j -= 1
      }
    }
    return result.reversed()
  }
}
