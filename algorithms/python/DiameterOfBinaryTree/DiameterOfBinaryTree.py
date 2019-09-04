# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.result = 0
        def dfs(node: TreeNode):
            if not node: return 0
            L = dfs(node.left)
            R = dfs(node.right)
            self.result = max(self.result, L+R)
            return max(L, R) + 1
        
        dfs(root)
        return self.result

########
# Test #
########

#       1
#      /  \
#     2    3
#    / \ 
#   4   5  
#  / \   \
# 6   7   8

root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(4)
node4 = TreeNode(5)
node5 = TreeNode(6)
node6 = TreeNode(7)
node7 = TreeNode(8)


root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node3.left = node5
node3.right = node6
node4.right = node7

assert Solution().diameterOfBinaryTree(root) == 4

print("OH, YEAH!")
