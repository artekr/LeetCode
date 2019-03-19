from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder:
            return None
        if len(postorder) == 1:
            return TreeNode(postorder[0])

        # the last element of the postorder always be root
		# with this thought, we want to divide original inorder and postorder array to conquer the problem
        root = TreeNode(postorder[-1])

        # Find out root index , so we can divide original inorder and postorder to smaller problem
        rootIndex = inorder.index(root.val)
        left_inorder = inorder[:rootIndex]
        right_inorder = inorder[rootIndex+1:]


        left_postorder = postorder[:rootIndex]
        right_postorder = postorder[rootIndex:len(postorder)-1]

        root.left = self.buildTree(left_inorder, left_postorder)
        root.right = self.buildTree(right_inorder, right_postorder)

        return root


# Recursive preorderTraversal
def preorderTraversal(root: TreeNode) -> List[int]:
    if root is None:
        return []
    result = []
    result.append(root.val)
    result += preorderTraversal(root.left)
    result += preorderTraversal(root.right)
    return result


########
# Test #
########

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

root = Solution().buildTree(inorder, postorder)

# expected:
#     3
#    / \
#   9  20
#     /  \
#    15   7

print(preorderTraversal(root))
# expected: [3, 9, 20, 15, 7]