from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root  = TreeNode(preorder[0])
        rootIndexInInorder = inorder.index(root.val)

        left_inorder = inorder[:rootIndexInInorder]
        right_inorder = inorder[rootIndexInInorder+1:]

        left_preorder = preorder[1:rootIndexInInorder+1]
        right_preorder = preorder[rootIndexInInorder+1:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root

# Recursive postorderTraversal
def postorderTraversal(root: TreeNode) -> List[int]:
    if root is None:
        return []
    result = []
    result += postorderTraversal(root.left)
    result += postorderTraversal(root.right)
    result.append(root.val)
    return result


########
# Test #
########

preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

root = Solution().buildTree(preorder, inorder)

# expected:
#     3
#    / \
#   9  20
#     /  \
#    15   7

print(postorderTraversal(root))
# expected: [9, 15, 7, 20, 3]