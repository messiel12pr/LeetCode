'''

    102. Binary Tree Level Order Traversal

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [root]
        levels = []

        if not root:
            return

        while queue:
            temp = []

            for i in range(len(queue)):
                curr = queue.pop(0)

                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)

                temp.append(curr.val)
                
            levels.append(temp)

        return levels
