from collections import deque
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        q = deque()
        q.append(root)
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level)
        result.reverse()
        return result

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

result = Solution().levelOrderBottom(root)
print(result)
# expected: [[15, 7], [9, 20], [3]]