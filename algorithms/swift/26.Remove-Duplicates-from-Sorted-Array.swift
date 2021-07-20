/**
 * Question Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
 * Time Complexity: O(n), Space Complexity: O(1)
 */

class Solution {
  func removeDuplicates(_ nums: inout [Int]) -> Int {
    print(nums.count)
    guard nums.count != 0 && nums.count != 1 else {
      print("count 0")
      return nums.count
    }
    var i = 0
    for j in 0..<nums.count {
      if nums[i] != nums[j] {
        i += 1
        nums[i] = nums[j]
      }
    }
    return i+1
  }
}

var nums: [Int] = []
// var nums = [1,2,3]
// var nums = [0,0,1,1,1,2,2,3,3,4]
Solution().removeDuplicates(&nums)
