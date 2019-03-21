# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#       5
#      / \
#     4   7
#    /   / \
#   1   6   8

root  = TreeNode(5)
node1 = TreeNode(4)
node2 = TreeNode(7)
node3 = TreeNode(1)
node4 = TreeNode(6)
node5 = TreeNode(8)

root.left = node1
root.right = node2
node1.left = node3
node2.left = node4
node2.right = node5

##########
# SEARCH #
##########

def BST_search(root: TreeNode, k: TreeNode):
    if not root or k.val == root.val:
        return root
    if k.val < root.val:
        return BST_search(root.left, k)
    else:
        return BST_search(root.right, k)

print("==== BST_search ====")
res = BST_search(root, TreeNode(9))
if res:
    print(res.val)
else:
    print("Not Found")
# expected: Not Found


###########
# MINIMUM #
###########

def BST_minimum(root: TreeNode):
    while root.left:
        root = root.left
    return root

print("==== BST_minimum ====")
res = BST_minimum(root)
print(res.val)
# expected: 1

###########
# MAXIMUM #
###########

def BST_maximum(root: TreeNode):
    while root.right:
        root = root.right
    return root

print("==== BST_maximum ====")
res = BST_maximum(root)
print(res.val)
# expected: 8

###########
# MAXIMUM #
###########

# def BST_maximum(root: TreeNode):