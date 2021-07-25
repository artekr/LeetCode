/**
 * Question Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
 */
 class Solution {
  /// Using Set
  /// Time Complexity: O(n), Space Complexity: O(n)
  func findDisappearedNumbers(_ nums: [Int]) -> [Int] {
    var uniqNums = Set<Int>(minimumCapacity: nums.count)
    for i in 1...nums.count {
      uniqNums.insert(i)
    }
    for n in nums {
      if uniqNums.contains(n) {
        uniqNums.remove(n)
      }
    }
    return Array(uniqNums)
  }
}


// print(Solution().findDisappearedNumbers([1,1]))
assert(Solution().findDisappearedNumbers([1,1]) == [2])
assert(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]) == [5,6])

print("PASS")
