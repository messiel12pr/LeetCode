'''

    113. Path Sum II

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def rec(node, path, path_sum):
            if not node:
                return

            path.append(node.val)
            path_sum += node.val

            if path_sum == targetSum and not node.left and not node.right:
                res.append(path.copy())

            rec(node.left, path.copy(), path_sum)
            rec(node.right, path.copy(), path_sum)

        rec(root, [], 0)
        return res