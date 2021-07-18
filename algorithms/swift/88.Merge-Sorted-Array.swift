//: 88 Merged Sorted Array
/**
 * Question Link: https://leetcode.com/problems/merge-sorted-array/
 *
 * Time Complexity: O(m+n), Space Complexity: O(1)
 */

class Solution {
  func merge(_ nums1: inout [Int], _ m: Int, _ nums2: [Int], _ n: Int) {
    guard m != 0 else {
      nums1 = nums2
      return
    }
    var i = m - 1
    var j = n - 1
    var last = m + n - 1
    while i >= 0 && j >= 0 {
      if nums1[i] > nums2[j] {
        nums1[last] = nums1[i]
        i -= 1
      } else {
        nums1[last] = nums2[j]
        j -= 1
      }
      last -= 1
    }
    /// For scenario 2
    while j >= 0 {
      nums1[j] = nums2[j]
      j -= 1
    }
  }

  func merge2(_ nums1: inout [Int], _ m: Int, _ nums2: [Int], _ n: Int) {
    guard m != 0 else {
      nums1 = nums2
      return
    }
    var i = m - 1
    var j = n - 1
    var last = m + n - 1
    /// Combine the condition
    while last >= 0 && j >= 0 {
      if i >= 0 && nums1[i] > nums2[j] {
        nums1[last] = nums1[i]
        i -= 1
      } else {
        nums1[last] = nums2[j]
        j -= 1
      }
      last -= 1
    }
  }
}

var n = [3,5,0,0,0]
Solution().merge(&n, 2, [1,2,4], 3)
