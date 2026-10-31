'''

    107. Binary Tree Level Order Traversal II

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        levels = []

        while queue:
            temp = []

            for i in range(len(queue)):
                curr_node = queue.pop(0)

                if curr_node.left:
                    queue.append(curr_node.left)

                if curr_node.right:
                    queue.append(curr_node.right)

                temp.append(curr_node.val)

            levels.append(temp)

        return reversed(levels) 
