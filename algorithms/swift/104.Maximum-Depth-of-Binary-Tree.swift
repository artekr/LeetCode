//: 104 Maximum Depth of Binary Tree
/**
 * Question Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
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
  /// Top-down approach, DFS, recursive
  func maxDepth_bfs(_ root: TreeNode?) -> Int {
    guard let root = root else { return 0 }

    var result = 1
    maxDepthChild(root, 1, &result)
    return result
  }

  private func maxDepthChild(_ node: TreeNode?, _ depth: Int, _ result: inout Int) {
    if let node = node {
      if node.left == nil && node.right == nil {
        result = max(result, depth)
      }
      maxDepthChild(node.left, depth + 1, &result)
      maxDepthChild(node.right, depth + 1, &result)
    }
  }

  /// Bottom-up approach, DFS, recursive
  func maxDepth_dfs(_ root: TreeNode?) -> Int {
    guard let root = root else { return 0 }

    return max(maxDepth_dfs(root.left), maxDepth_dfs(root.right)) + 1
  }

  /// Iteration, level order traversal
  func maxDepth_iteration(_ root: TreeNode?) -> Int {
    guard let root = root else { return 0 }

    var queue = [root]
    var result = 0
    while !queue.isEmpty {
      for node in queue {
        let n = queue.removeFirst()
        if let left = n.left { queue.append(left) }
        if let right = n.right { queue.append(right) }
      }
      result += 1
    }
    return result
  }
}
