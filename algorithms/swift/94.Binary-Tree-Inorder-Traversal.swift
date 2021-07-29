//: 94 Binary Tree Inorder Traversal
/**
 * Question Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
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
  // recursion
  func inorderTraversal(_ root: TreeNode?) -> [Int] {
    guard let root = root else { return [] }

    var result = [Int]()
    result += inorderTraversal(root.left)
    result.append(root.val)
    result += inorderTraversal(root.right)
    return result
  }

  // iteration, using stack to store the parent node
  func inorderTraversal2(_ root: TreeNode?) -> [Int] {
    var current = root
    var stack = [TreeNode]()
    var result = [Int]()

    while current != nil || !stack.isEmpty {
      while let node = current {
        stack.append(node)
        current = node.left
      }
      if let node = stack.popLast() {
        result.append(node.val)
        current = node.right
      }
    }

    return result
  }
}
