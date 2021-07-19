/**
 * Question Link: https://leetcode.com/problems/remove-element/
 * Time Complexity: O(n), Space Complexity: O(1)
 */

class Solution {
  /// Two pointers
  func removeElement(_ nums: inout [Int], _ val: Int) -> Int {
    var i = 0
    var j = nums.count - 1
    while i <= j {
      if nums[i] == val {
        nums[i] = nums[j]
        j -= 1
      } else {
        i += 1
      }
    }
    return j+1
  }

  /// Two Pointers - copy over elements
  func removeElement2(_ nums: inout [Int], _ val: Int) -> Int {
    var cur = 0
    for n in nums {
      if n != val {
        nums[cur] = n
        cur += 1
      }
    }
    return cur
  }
}

var nums = [0,1,2,2,3,0,4,2]
print(Solution().removeElement(&nums, 2))
// [0, 1, 4, 0, 3, -1, -1, -1]
