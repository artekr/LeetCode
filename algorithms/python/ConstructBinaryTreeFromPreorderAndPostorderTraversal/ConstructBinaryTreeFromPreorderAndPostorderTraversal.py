from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])

        root = TreeNode(pre[0])
        # pre[1] will be root node on the left branch, post.index(pre[1]) indicates location in post, and post.index(pre[1]) + 1 will be numble of node in left branch
        L = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1:L+1], post[:L])
        root.right = self.constructFromPrePost(pre[L+1:], post[L:])
    
        return root

        # if not pre:
        #     return None
        # if len(pre) == 1:
        #     return TreeNode(pre[0])

        # li = 0
        # ri = len(post) - 1
        # root = TreeNode(pre[li])

        # if pre[li+1] != post[ri-1]:
        #     left_pre = pre[1:li+2]
        #     left_post = post[:1]

        #     right_pre = pre[li+2:]
        #     right_post = post[1:ri]

        #     root.left = self.constructFromPrePost(left_pre, left_post)
        #     root.right = self.constructFromPrePost(right_pre, right_post)
        # else:
        #     root.left = self.constructFromPrePost(pre[li+1:], post[:ri])
            
        # return root

# Recursive inorderTraversal
def inorderTraversal(root: TreeNode) -> List[int]:
    if root is None:
        return []
    result = []
    result += inorderTraversal(root.left)
    result.append(root.val)
    result += inorderTraversal(root.right)
    return result


########
# Test #
########

pre = [1,2,4,5,3,6,7]
post = [4,5,2,6,7,3,1]

root = Solution().constructFromPrePost(pre, post)

# expected:
#     3
#    / \
#   9  20
#     /  \
#    15   7

print(inorderTraversal(root))
# expected: [9, 3, 15, 20, 7]