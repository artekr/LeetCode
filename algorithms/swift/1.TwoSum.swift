/**
 * Question Link: https://leetcode.com/problems/two-sum/
 *
 * Use a hashmap with one pass iteration, try to find the complement
 *
 * Time Complexity: O(n), Space Complexity: O(n)
 */

class Solution {
  func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
    var dict: [Int: Int] = [:]
    for (i, num) in nums.enumerated() {
      if let complementIndex = dict[target - num] {
        return [complementIndex, i]
      }
      dict[num] = i
    }
    fatalError("No solution found")
  }
}

print(Solution().twoSum([3,2,4], 6))
// [1, 2]
