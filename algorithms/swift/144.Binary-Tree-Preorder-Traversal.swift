//: 144 Binary Tree Preorder Traversal
/**
 * Question Link: https://leetcode.com/problems/binary-tree-preorder-traversal/
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
  /// recursion
  func preorderTraversal(_ root: TreeNode?) -> [Int] {
    guard let root = root else { return [] }

    var result = [Int]()
    result.append(root.val)
    result += preorderTraversal(root.left)
    result += preorderTraversal(root.right)
    return result
  }

  /// iteration, using a stack to store the right child
  func preorderTraversal2(_ root: TreeNode?) -> [Int] {
    var current = root
    var stack = [TreeNode?]()
    var result = [Int]()
    while true {
      if let c = current {
        result.append(c.val)
        stack.append(c.right)
        current = c.left
      } else if !stack.isEmpty {
        current = stack.removeLast()
      } else {
        break
      }
    }
    return result
  }
}
