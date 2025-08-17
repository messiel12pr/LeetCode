'''

    988. Smallest String Starting From Leaf

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        paths = []
        def rec(node, path):
            if not node:
                return

            path.insert(0, chr(node.val + ord('a')))
            if not node.left and not node.right:
                paths.append(''.join(path))

            rec(node.left, path.copy())
            rec(node.right, path.copy())

        rec(root, [])
        return min(paths)