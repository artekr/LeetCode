# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.checkNodes(root.left, root.right)

    def checkNodes(self, node1, node2):
        if not node1 and not node2:
            return True
        elif not node1 or not node2:
            return False
        
        return node1.val == node2.val and self.checkNodes(node1.left, node2.right) and self.checkNodes(node1.right, node2.left)

########
# Test #
########

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3

root  = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(4)
node6 = TreeNode(3)

root.left   = node1
root.right  = node2
node1.left  = node3
node1.right = node4
node2.left  = node5
node2.right = node6

result = Solution().isSymmetric(root)
print(result)
# expected: True

#    1
#   / \
#  2   2
#   \   \
#   3    3

# root = TreeNode(1)
# node1 = TreeNode(2)
# node2 = TreeNode(2)
# node3 = TreeNode(3)
# node4 = TreeNode(3)

# root.left = node1
# root.right = node2
# node1.right = node3
# node2.right = node4

# expected: False
