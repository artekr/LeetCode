# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.total = 0

    # Recursion
    def convertBST(self, root: TreeNode) -> TreeNode:
        # Perform a "in order traversal", but starting from right to left
        if root:
            self.convertBST(root.right)
            self.total += root.val
            root.val = self.total
            self.convertBST(root.left)
        return root

    # Iteration
    def convertBST_iteration(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        stack = []
        total = 0
        current = root
        while True:
            while current:
                stack.append(current)
                current = current.right
            if not stack:
                return root
            node = stack.pop()
            total += node.val
            node.val = total
            current = node.left

########
# Test #
########

#    5
#   /  \
#  2   13

root = TreeNode(5)
node1 = TreeNode(2)
node2 = TreeNode(13)

root.left = node1
root.right = node2

# new_root = Solution().convertBST(root)
new_root = Solution().convertBST_iteration(root)

assert new_root.val == 18
assert new_root.left.val == 20
assert new_root.right.val == 13

print("OH, YEAH!")

#    18
#   /  \
#  20   13