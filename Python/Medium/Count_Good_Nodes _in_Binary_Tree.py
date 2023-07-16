'''

    1448. Count Good Nodes in Binary Tree

    Solution

'''

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def count_good_nodes(root, max):
            if root == None: 
                return

            if root.val >= max:
                max = root.val
                nonlocal count 
                count += 1

            count_good_nodes(root.left, max)
            count_good_nodes(root.right, max)
    
        count_good_nodes(root, -sys.maxsize-1)
        return count