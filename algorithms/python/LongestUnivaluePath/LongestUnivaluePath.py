# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0
        
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            l = l+1 if node.left and node.left.val == node.val else 0
            r = r+1 if node.right and node.right.val == node.val else 0
            self.ans = max(self.ans, l+r)
            return max(l, r)
        dfs(root)
        return self.ans