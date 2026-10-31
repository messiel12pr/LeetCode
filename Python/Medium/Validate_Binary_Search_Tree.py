'''

    98. Validate Binary Search Tree

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nums = []
        def rec(node):
            if not node:
                return

            rec(node.left)
            nonlocal nums
            nums.append(node.val)
            rec(node.right)

        rec(root)
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                return False
        return True
        
