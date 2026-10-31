'''

    783. Minimum Distance Between BST Nodes

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def in_order(root: Optional[TreeNode], nums: list):
            if not root:
                return

            in_order(root.left, nums)
            nums.append(root.val)
            in_order(root.right, nums)

        min_diff = sys.maxsize
        sorted_elements = []
        in_order(root, sorted_elements)

        for i in range(len(sorted_elements) - 1):
            current_diff = sorted_elements[i+1] - sorted_elements[i]
            if current_diff < min_diff:
                min_diff = current_diff

        return min_diff


        
