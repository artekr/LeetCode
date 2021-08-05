//: 226 Invert Binary Tree
/**
 * Question Link: https://leetcode.com/problems/invert-binary-tree/
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
  // Preorder invert
  func invertTree_pre(_ root: TreeNode?) -> TreeNode? {
    guard let root = root else { return nil }

    // Swap the children of the current node first, then recursively inverting its left and right child
    let temp = root.left
    root.left = root.right
    root.right = temp

    invertTree(root.left)
    invertTree(root.right)
    return root
  }

  // Postorder invert
  func invertTree_post(_ root: TreeNode?) -> TreeNode? {
    guard let root = root else { return nil }

    // Recursively calling the inverting of the left and right child of the node first, then doing the actual swap.
    let left = invertTree(root.left)
    let right = invertTree(root.right)
    root.left = right
    root.right = left
    return root
  }
}
