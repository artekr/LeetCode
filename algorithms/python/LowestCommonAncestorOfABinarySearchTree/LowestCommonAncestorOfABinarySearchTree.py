# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Recursive
class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Value of the current node or root node
        parent_val = root.val

        # values of node p and q
        p_val = p.val
        q_val = q.val

        # If both p and q are greater than parent
        if p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right, p, q)
        # If both p and q are lesser than parent
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)
        # We have found the split point, i.e. the LCA node.
        else:
            return root

# Iterative
class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # values of node p and q
        p_val = p.val
        q_val = q.val

        current = root

        while current:
            # Value of the current node or root node
            parent_val = current.val
            if p_val > parent_val and q_val > parent_val:
                current = current.right
            elif p_val < parent_val and q_val < parent_val:
                current = current.left
            else:
                return current


########
# Test #
########

#     2
#    / \
#   0   4
#      / \
#     3   5

root = TreeNode(2)
node1 = TreeNode(0)
node2 = TreeNode(4)
node3 = TreeNode(3)
node4 = TreeNode(5)

root.left = node1
root.right = node2
node2.left = node3
node2.right = node4

result = Solution1().lowestCommonAncestor(root, node1, node4)
print(result.val)
# expected: root, 2

result = Solution2().lowestCommonAncestor(root, node2, node3)
print(result.val)
# expected: root, 4