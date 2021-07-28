/**
 * Question Link: https://leetcode.com/problems/third-maximum-number/
 */
class Solution {
  /// Sort the array first
  /// Time Complexity: O(nlogn), Space Complexity: O(n)
  func thirdMax(_ nums: [Int]) -> Int {
    guard nums.count > 1 else { return nums[0] }
    var sorted = nums
    sorted.sort(by: >)
    var counter = 1
    var thirdMax = sorted[0]
    for n in sorted {
      if n < thirdMax {
        thirdMax = n
        counter += 1
      }
      if counter == 3 {
        return thirdMax
      }
    }
    return sorted[0]
  }
}

assert(Solution().thirdMax([2,2,3,1]) == 1)
assert(Solution().thirdMax([1,2,1,1]) == 2)
assert(Solution().thirdMax([2,2,3]) == 3)

print("PASS")
