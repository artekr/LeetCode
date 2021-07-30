//: 102 Binary Tree Level Order Traversal
/**
 * Question Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
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
  /// BFS
  func levelOrder(_ root: TreeNode?) -> [[Int]] {
    guard root != nil else { return [] }

    var queue = [root]
    var result = [[Int]]()
    while !queue.isEmpty {
      var levels = [Int]()
      for node in queue {
        if let n = queue.removeFirst() {
          levels.append(n.val)
          if let left = n.left { queue.append(left) }
          if let right = n.right { queue.append(right) }
        }
      }
      result.append(levels)
    }
    return result
  }
}
