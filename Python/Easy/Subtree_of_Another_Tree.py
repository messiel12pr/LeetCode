'''

  572. Subtree of Another Tree

  Solution:
  
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def compare_tree(sub_tree, subRoot):
    if not sub_tree and not subRoot:
        return True

    if not sub_tree or not subRoot:
        return False

    if sub_tree.val == subRoot.val:
        return compare_tree(sub_tree.left, subRoot.left) and compare_tree(sub_tree.right, subRoot.right)
    
    return False

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if root.val == subRoot.val and compare_tree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
