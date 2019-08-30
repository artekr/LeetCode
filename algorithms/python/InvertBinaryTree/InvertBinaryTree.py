# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        l = self.invertTree(root.left)
        r = self.invertTree(root.right)
        root.right = l
        root.left = r
        return root

    def invertTree_BFS(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            tmp = node.left
            node.left = node.right
            node.right = tmp
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)        
        return root
