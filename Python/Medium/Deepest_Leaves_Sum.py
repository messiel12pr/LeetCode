'''

    1302. Longest Substring Without Repeating Characters

    Solution:

        Level order traversal, keep track of leaf sum and reset sum 
        when finding non-leaf node
        
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        leaf_sum = 0

        while queue:
            temp = []
            not_deepest = False

            while queue:
                curr_node = queue.pop(0)    

                if not not_deepest and not curr_node.left and not curr_node.right:
                    leaf_sum += curr_node.val

                else:
                    leaf_sum = 0
                    not_deepest = True

                if curr_node.left:
                    temp.append(curr_node.left)

                if curr_node.right:
                    temp.append(curr_node.right)

            queue = temp

        return leaf_sum