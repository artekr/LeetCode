//: 116 Populating Next Right Pointers in Each Node
/**
 * Question Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
 */

/**
 * Definition for a Node.
 * public class Node {
 *     public var val: Int
 *     public var left: Node?
 *     public var right: Node?
 *	   public var next: Node?
 *     public init(_ val: Int) {
 *         self.val = val
 *         self.left = nil
 *         self.right = nil
 *         self.next = nil
 *     }
 * }
 */

/*
     1
   /  \
  2    3
 / \  / \
4  5 6  7
*/

class Solution {
  func connect(_ root: Node?) -> Node? {
    guard let root = root else { return nil }

    root.left?.next = root.right
    // bridge the children of their parent nodes, 5 -> 6
    root.right?.next = root.next?.left

    connect(root.left)
    connect(root.right)
    return root
  }

  /// with a helper function to connect two child nodes
  func connect_top_down(_ root: Node?) -> Node? {
    guard let root = root else { return nil }
    connect(node1: root.left, with: root.right)
    return root
  }

  private func connect(node1: Node?, with node2: Node?) {
    guard let leftNode = node1, let rightNode = node2 else { return }

    // Similar to pre order traversal
    leftNode.next = rightNode
    // connect the children of each node
    connect(node1: leftNode.left, with: leftNode.right)
    connect(node1: rightNode.left, with: rightNode.right)
    // bridge the children of the two nodes, 5 -> 6
    connect(node1: leftNode.right, with: rightNode.left)
  }
}
