# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        return self.helper(root, sum, 0)
        
    def helper(self, node, sum, current):
        if not node:
            return current == sum
        current += node.val
        self.helper(node.left, sum, current)
        self.helper(node.right, sum, current)
