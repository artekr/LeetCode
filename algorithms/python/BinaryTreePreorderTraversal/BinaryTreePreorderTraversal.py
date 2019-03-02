# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# recursive
class Solution1:
    def preorderTraversal(self, root: TreeNode):
        if not root:
          return []
        result = []
        result.append(root.val)
        result += self.preorderTraversal(root.left)
        result += self.preorderTraversal(root.right)
        return result

# iteration
class Solution2:
    def preorderTraversal(self, root: TreeNode):
        current = root
        stack = []
        result = []
        
        while True:
            if current is not None:
                result.append(current.val)
                stack.append(current.right)
                current = current.left
            elif len(stack):
                current = stack.pop()
            else:
                break
        
        return result