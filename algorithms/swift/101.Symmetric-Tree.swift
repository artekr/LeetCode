//: 101 Symmetric Tree
/**
 * Question Link: https://leetcode.com/problems/symmetric-tree/
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
  /// Top-down, DFS
  func isSymmetric(_ root: TreeNode?) -> Bool {
    guard let root = root else { return true }
    return checkChildren(root.left, root.right)
  }

  private func checkChildren(_ node1: TreeNode?, _ node2: TreeNode?) -> Bool {
    if node1 == nil && node2 == nil { return true }
    if node1 == nil || node2 == nil { return false }

    return node1!.val == node2!.val && checkChildren(node1!.left, node2!.right) && checkChildren(node1!.right, node2!.left)
  }

  /// Top-down, BFS, iteration
  func isSymmetric_iteration(_ root: TreeNode?) -> Bool {
    guard let root = root else { return true }

    var queue: [TreeNode?] = [root, root]
    while !queue.isEmpty {
      let n1 = queue.removeFirst()
      let n2 = queue.removeFirst()
      if n1 == nil && n2 == nil { continue }
      if n1 == nil || n2 == nil { return false }
      if n1?.val != n2?.val { return false }
      queue.append(n1?.left)
      queue.append(n2?.right)
      queue.append(n1?.right)
      queue.append(n2?.left)
    }
    return true
  }
}
