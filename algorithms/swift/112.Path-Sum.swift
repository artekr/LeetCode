//: 112 Path Sum
/**
 * Question Link: https://leetcode.com/problems/path-sum/
 */

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init() { self.val = 0; self.left = nil; self.right = nil; }
 *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
 *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
 *         self.val = val
 *         self.left = left
 *         self.right = right
 *     }
 * }
 */
class Solution {
  func hasPathSum(_ root: TreeNode?, _ targetSum: Int) -> Bool {
    guard let root = root else { return false }
    var result = [Int]()
    calculateSums(root, root.val, &result)
    return result.contains(targetSum)
  }

  // Calculate all the possible sums at each leaf node
  private func calculateSums(_ node: TreeNode?, _ currentSum: Int, _ result: inout [Int]) {
    guard let node = node else { return }
    if node.left == nil && node.right == nil {
      result.append(currentSum)
      return
    }
    calculateSums(node.left, currentSum+(node.left?.val ?? 0), &result)
    calculateSums(node.right, currentSum+(node.right?.val ?? 0), &result)
  }

  /// Recursive, substract the val at each node
  func hasPathSum_dfs(_ root: TreeNode?, _ targetSum: Int) -> Bool {
    guard let root = root else { return false }
    // if it is a leaf node, and substracting its value equal to 0, means we find a match
    if (targetSum - root.val == 0) && root.left == nil && root.right == nil { return true }

    return hasPathSum(root.left, targetSum - root.val) || hasPathSum(root.right, targetSum - root.val)
  }
}
