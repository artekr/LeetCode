//: 94 Binary Tree Postorder Traversal
/**
 * Question Link: https://leetcode.com/problems/binary-tree-postorder-traversal/
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
  func postorderTraversal(_ root: TreeNode?) -> [Int] {
    guard let root = root else { return [] }

    var result = [Int]()
    result += postorderTraversal(root.left)
    result += postorderTraversal(root.right)
    result.append(root.val)
    return result
  }

  // iteration, using a queue
  func postorderTraversal2(_ root: TreeNode?) -> [Int] {
    guard let root = root else { return [] }

    var stack = [root]
    // shoule be using a Deque
    var result = [Int]()
    while !stack.isEmpty {
      if let current = stack.popLast() {
        // similar to prepend method in Deque.
        result.insert(current.val, at: 0)
        if let left = current.left {
          stack.append(left)
        }
        if let right = current.right {
          stack.append(right)
        }
      }
    }
    return Array(result)
  }
}
