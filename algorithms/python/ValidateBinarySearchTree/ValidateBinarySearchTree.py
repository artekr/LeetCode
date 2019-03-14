from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        valueArray = []
        self.inorderTraversal(root, valueArray)
        if len(valueArray) > 1:
            for i in range(0, len(valueArray)-1):
                if valueArray[i] >= valueArray[i+1]:
                    return False
        return True
        
    def inorderTraversal(self, root: TreeNode, valArray: List[int]):
        if not root:
            return []
        if root.left:
            self.inorderTraversal(root.left, valArray)
        valArray.append(root.val)
        if root.right:
            self.inorderTraversal(root.right, valArray)
        return valArray



########
# Test #
########

# Empty Tree

print(Solution().isValidBST(None))
# expected: True

##################################

#     0

root  = TreeNode(0)

print(Solution().isValidBST(root))
# expected: True

##################################

#   1
#  /
# 1

root  = TreeNode(1)
node1  = TreeNode(1)

root.left = node1

print(Solution().isValidBST(root))
# expected: False

##################################

#     2
#    / \
#   1   3

root  = TreeNode(2)
node1 = TreeNode(1)
node2 = TreeNode(3)
root.left = node1
root.right = node2

print(Solution().isValidBST(root))
# expected: True

##################################

#       5
#      / \
#     1   4
#        / \
#       3   6

root  = TreeNode(5)
node1 = TreeNode(1)
node2 = TreeNode(4)
node3 = TreeNode(3)
node4 = TreeNode(6)

root.left = node1
root.right = node2
node2.left = node3
node2.right = node4

print(Solution().isValidBST(root))
# expected: False

##################################

#       5
#      / \
#     4   7
#    /   / \
#   1   6   8

root  = TreeNode(5)
node1 = TreeNode(4)
node2 = TreeNode(7)
node3 = TreeNode(1)
node4 = TreeNode(6)
node5 = TreeNode(8)

root.left = node1
root.right = node2
node1.left = node3
node2.left = node4
node2.right = node5

print(Solution().isValidBST(root))
# expected: True