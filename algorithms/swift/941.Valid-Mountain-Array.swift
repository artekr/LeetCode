//: 941 Valid Mountain Array
/**
 * Question Link: https://leetcode.com/problems/valid-mountain-array/
 *
 * Time Complexity: O(n), Space Complexity: O(1)
 */

class Solution {
  func validMountainArray(_ arr: [Int]) -> Bool {
    guard arr.count > 2 else { return false }

    var peak = 0
    // First iteration to find the peak
    for i in 0..<(arr.count-1) {
      // if ever encounter the next value is equal to the current one, return false
      if arr[i+1] == arr[i] {
        return false
      } else if arr[i+1] < arr[i] {
        // if the next one is smaller than the current one, then we find the peak
        peak = i
        break
      }
    }
    // we need to make sure the peak is neither the first one nor the last one
    // [1,2,3] -> false
    // [3,2,1] -> false
    if peak == 0 || peak == arr.count-1 {
      return false
    }
    // starting with the peak, the following values should getting smaller
    for j in peak..<(arr.count-1) {
      // if the enxt value is greater or equal to the current one, return false
      if arr[j+1] >= arr[peak] {
        return false
      }
      // otherwise move the current to the next one
      peak += 1
    }
    // Default to true
    return true
  }

  func validMountainArray2(_ arr: [Int]) -> Bool {
    guard arr.count > 2 else { return false }

    var i = 0
    let j = arr.count
    // keep one index, if next one is greater than the current one, increase the index
    while i+1 < j && arr[i] < arr[i+1] {
      i += 1
    }
    // we need to make sure the peak is neither the first one nor the last one
    // [1,2,3] -> false
    // [3,2,1] -> false
    if i == 0 || i == j-1 {
      return false
    }
    // at this point i should be the peak, values following should be in a decreasing order
    while i+1 < j && arr[i] > arr[i+1] {
      i += 1
    }
    // only iterating through the whole array that we consider it's a valid mountain array
    return i == j-1
  }
}

let n = [1,2,3,2,1]
// let n = [1,2,3,2]
// let n = [1,2,2]
// let n = [2,0,2]

// let n = [1,2,3,4,5]
// let n = [5,4,3,2,1]

print(Solution().validMountainArray2(n))
