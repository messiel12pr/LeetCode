'''

    105. Construct Binary Tree from Preorder and Inorder Traversal

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        positions = {val:idx for idx, val in enumerate(inorder)}
        idx = 0
        def rec(l, r):
            if l > r:
                return None 

            nonlocal idx
            new_node = TreeNode(preorder[idx])

            idx += 1
            pos = positions[new_node.val]
            new_node.left = rec(l, pos - 1)
            new_node.right = rec(pos + 1, r)
            return new_node

        return rec(0, len(preorder) - 1)
