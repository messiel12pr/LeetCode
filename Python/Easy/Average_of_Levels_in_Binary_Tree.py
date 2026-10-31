'''

    637. Average of Levels in Binary Tree

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = [root]
        averages = []

        while queue:
            level_sum = 0
            lenght = len(queue)

            for c in range(len(queue)):
                curr_node = queue.pop(0)
                level_sum += curr_node.val 

                if curr_node.left:
                    queue.append(curr_node.left)

                if curr_node.right:
                    queue.append(curr_node.right)

            averages.append(level_sum/lenght)

        return averages
