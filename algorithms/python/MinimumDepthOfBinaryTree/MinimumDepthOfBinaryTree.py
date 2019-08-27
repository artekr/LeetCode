from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = deque([(root, 1)])
        while q:
            node,result = q.popleft()
            if node.left is None and not node.right:
                return result
            else:
                if node.left:
                    q.append((node.left, result+1))
                if node.right:
                    q.append((node.right, result+1))

########
# Test #
########

#       3
#      / \
#     9   20
#        /  \
#       15   7

root = TreeNode(3)
node1 = TreeNode(9)
node2 = TreeNode(20)
node3 = TreeNode(15)
node4 = TreeNode(7)

root.left = node1
root.right = node2
node2.left = node3
node2.right = node4

result = Solution().minDepth(root)
print(result)
# expected: 3