'''

    872. Leaf-Similar Trees

    Solution:

'''

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def traverse(root, arr):
            if root == None: return

            traverse(root.left, arr)
            if root.left == None and root.right == None:
                arr.append(root.val)
            traverse(root.right, arr)

        list_1 = []
        list_2 = []

        traverse(root1, list_1)
        traverse(root2, list_2)

        return list_1 == list_2