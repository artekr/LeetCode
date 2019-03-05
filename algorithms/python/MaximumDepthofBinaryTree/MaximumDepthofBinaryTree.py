# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# DFS recursion (Bottom up solution)
class Solution1:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1

# DFS Iteration
class Solution2:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

# BFS Iteration
class Solution3:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0



########
# Test #
########

#     3
#    / \
#   9  20
#     /  \
#    15   7

root = TreeNode(3)
node1 = TreeNode(9)
node2 = TreeNode(20)
node3 = TreeNode(15)
node4 = TreeNode(7)

root.left = node1
root.right = node2
node2.left = node3
node2.right = node4

result = Solution1().maxDepth(root)
print(result)
# expected: 3