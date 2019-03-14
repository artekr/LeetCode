# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Iterative
class Solution1:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        succ = None
        while root:
            if p.val < root.val:
                succ = root
                root = root.left
            else:
                root = root.right
        return succ

# Recursive

class Solution2:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        if p.val < root.val:
            return self.inorderSuccessor(root.left, p) or root
        return self.inorderSuccessor(root.right, p)



########
# Test #
########

#     2
#    / \
#   1   3

root  = TreeNode(2)
node1 = TreeNode(1)
node2 = TreeNode(3)
root.left = node1
root.right = node2

p = TreeNode(1)

print(Solution2().inorderSuccessor(root, p).val)
# expected: 2

#     2
#      \
#       3

root  = TreeNode(2)
node1 = TreeNode(3)
root.right = node1

p = TreeNode(2)

print(Solution2().inorderSuccessor(root, p).val)
# expected: 2

#       5
#      / \
#     3   6
#    / \
#   2   4
#  /
# 1

root  = TreeNode(5)
node1 = TreeNode(3)
node2 = TreeNode(6)
node3 = TreeNode(2)
node4 = TreeNode(4)
node5 = TreeNode(1)

root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node3.left = node5

p = TreeNode(6)

print(Solution2().inorderSuccessor(root, p))
# expected: None
