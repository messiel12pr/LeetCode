'''

    235. Lowest Common Ancestor of a Binary Search Tree

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if root.val <= p.val and root.val >= q.val or root.val >= p.val and root.val <= q.val:
                return root

            elif root.val > p.val and root.val > q.val:
                root = root.left

            else:
                root = root.right

        return None