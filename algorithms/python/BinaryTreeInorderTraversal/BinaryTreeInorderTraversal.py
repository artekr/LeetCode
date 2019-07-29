from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Recursive
class Solution1:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        result = []
        result += self.inorderTraversal(root.left)
        result.append(root.val)
        result += self.inorderTraversal(root.right)
        return result

# iteration
class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, result = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return result
            node = stack.pop()
            result.append(node.val)
            root = node.right

########
# Test #
########

#     1
#    / \
#   2   3
#  /  \
# 4    5
#     /
#    6

root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(4)
node4 = TreeNode(5)
node5 = TreeNode(6)

root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node4.left = node5

result = Solution2().inorderTraversal(root)
print(result)
# expected: [4, 2, 6, 5, 1, 3]