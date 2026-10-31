'''

    230. Kth Smallest Element in a BST

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_tree_values = []

        def in_order(root):
            if not root:
                return

            in_order(root.left)
            sorted_tree_values.append(root.val)
            in_order(root.right)

        in_order(root)

        return sorted_tree_values[k - 1]
