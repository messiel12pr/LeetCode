'''

    257. Binary Tree Paths

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        def rec(node, path):
            if not node:
                return

            path.append(str(node.val))
            if not node.left and not node.right:
                paths.append(path.copy())

            rec(node.right, path.copy())
            rec(node.left, path.copy())

        rec(root, [])
        res = []
        for path in paths:
            res.append("->".join(path))
        return res