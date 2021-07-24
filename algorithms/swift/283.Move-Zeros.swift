/**
 * Question Link: https://leetcode.com/problems/move-zeroes/
 * Time Complexity: O(n), Space Complexity: O(1)
 */
class Solution {
  func moveZeroes(_ nums: inout [Int]) {
    guard nums.count != 1 else { return }

    var i = 0
    for j in 1..<nums.count {
      if nums[i] == 0 {
        if nums[j] != 0 {
          nums.swapAt(i,j)
          i += 1
        }
      } else {
        i += 1
      }
    }
    print(nums)
  }

  func moveZeroes2(_ nums: inout [Int]) {
    guard nums.count != 1 else { return }

    var lastZeroIndex = 0
    for cur in 0..<nums.count {
      if nums[cur] != 0 {
        nums.swapAt(lastZeroIndex, cur)
        lastZeroIndex += 1
      }
    }
    print(nums)
  }
}

var n = [0,1,0,3,12]
// var n = [0]
print(Solution().moveZeroes2(&n))
