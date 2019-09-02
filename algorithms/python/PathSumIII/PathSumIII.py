# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        

    def helper(self, node: TreeNode, sum: int, current: int) -> bool:
 

########
# Test #
########

#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1

root = TreeNode(10)
node1 = TreeNode(5)
node2 = TreeNode(-3)
node3 = TreeNode(3)
node4 = TreeNode(2)
node5 = TreeNode(11)
node6 = TreeNode(3)
node7 = TreeNode(-2)
node8 = TreeNode(1)

root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node2.right = node5
node3.left = node6
node3.right = node7
node4.right = node8

assert Solution().pathSum(root, 8) == 3

print("Oh YEAH!")
