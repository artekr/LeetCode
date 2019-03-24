# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Recursive
class Solution1:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val = t1.val + t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

# Iterative
class Solution2:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        stack = [(t1, t2)]
        while stack:
            t = stack.pop()
            if not t[0] or not t[1]:
                continue
            t[0].val += t[1].val
            if not t[0].left:
                t[0].left = t[1].left
            else:
                stack.append((t[0].left, t[1].left))
            if not t[0].right:
                t[0].right = t[1].right
            else:
                stack.append((t[0].right, t[1].right))
        return t1


# Tree 1                     Tree 2                  
#       1                         2                             
#      / \                       / \                            
#     3   2                     1   3                        
#    /                           \   \                      
#   5                             4   7                  

# Tree 1
t1 = TreeNode(1)
t11 = TreeNode(3)
t12 = TreeNode(2)
t13 = TreeNode(1)

t1.left = t11
t1.right = t12
t11.left = t13

# Tree 2
t2 = TreeNode(2)
t21 = TreeNode(1)
t22 = TreeNode(3)
t23 = TreeNode(4)
t24 = TreeNode(7)

t2.left = t21
t2.right = t22
t21.right = t23
t22.right = t24

print(Solution1().mergeTrees(t1, t2))

# Expected Merged tree:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \ 
# 	 5   4   7