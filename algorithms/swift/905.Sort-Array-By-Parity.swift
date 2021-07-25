/**
 * Question Link: https://leetcode.com/problems/sort-array-by-parity/
 */
class Solution {
  /// One pass, wiht new array
  /// Time Complexity: O(n), Space Complexity: O(n)
  func sortArrayByParity(_ nums: [Int]) -> [Int] {
    guard nums.count > 1 else { return nums }

    var result = [Int](repeating: 0, count: nums.count)
    var i = 0
    var j = nums.count-1
    for n in nums {
      if n % 2 == 0 {
        result[i] = n
        i += 1
      } else {
        result[j] = n
        j -= 1
      }
    }
    return result
  }

  /// In place, two pointers
  /// Time Complexity: O(n), Space Complexity: O(1)
  func sortArrayByParity2(_ nums: inout [Int]) -> [Int] {
    guard nums.count > 1 else { return nums }
    var i = 0
    var j = nums.count-1
    while i < j {
      if nums[i] % 2 == 1 && nums[j] % 2 == 0 {
        nums.swapAt(i,j)
        i += 1
        j -= 1
      }
      if nums[i] % 2 == 0 { i += 1 }
      if nums[j] % 2 == 1 { j -= 1 }
    }
    return nums
  }
}

assert(Solution().sortArrayByParity([3,1,2,4]) == [2,4,1,3])
assert(Solution().sortArrayByParity([3]) == [3])
assert(Solution().sortArrayByParity([3,4,1,2,5,7,8,10]) == [4, 2, 8, 10, 7, 5, 1, 3])

print("PASS")