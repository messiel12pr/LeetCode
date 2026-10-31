'''

    450. Delete Node in a BST

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def find_min_node(root):
    if not root:
        return 

    if not root.left:
        return root

    return find_min_node(root.left)


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        elif key < root.val:
            root.left = self.deleteNode(root.left, key)

        else:
            if not root.left:
                return root.right

            elif not root.right:
                return root.left

            root.val = find_min_node(root.right).val
            root.right = self.deleteNode(root.right, root.val)

        return root
