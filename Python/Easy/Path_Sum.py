'''

    112. Path Sum

    Solution
    
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

found = False
def in_order(node, sum, target):
    if node == None:
        return 

    sum += node.val

    if node.left == None and node.right == None and sum == target:
        global found
        found = True

    elif node.left == None and node.right == None:
        sum -= node.val
        
    in_order(node.left, sum, target) 
    in_order(node.right, sum, target) 

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        global found
        found = False

        in_order(root, 0, targetSum)
        return found
