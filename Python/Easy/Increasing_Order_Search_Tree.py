"""

    897. Increasing Order Search Tree

    Solution:

"""

def inOrder(r: TreeNode, s: List):
    if r == None:
        return

    inOrder(r.left, s)
    r.left = None
    s.append(r)
    inOrder(r.right, s)

class Solution:

    def increasingBST(self, root: TreeNode) -> TreeNode:
        s = []
        inOrder(root, s)
        root = s[0]

        for i in range(len(s)-1):
            s[i].right = s[i+1]

        return root
