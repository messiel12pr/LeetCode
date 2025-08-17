'''

    101. Symmetric Tree

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = [root]

        while queue:
            next_layer = queue.copy()
            queue.clear()
            tree = []
            while next_layer:
                curr = next_layer.pop(0)
                if curr:
                    tree.append(curr.val)

                else:
                    tree.append(None)
                if curr:
                    queue.append(curr.left)
                    queue.append(curr.right)

            for i in range(len(tree)):
                if tree[i] != tree[len(tree) - i - 1]:
                    return False

        return True 