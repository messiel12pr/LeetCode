'''

    430. Flatten a Multilevel Doubly Linked List

'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        res = []
        def dfs(root):
            visited = set()
            stack = [root]

            while stack:
                node = stack.pop()
                if not node:
                    continue
                res.append(node)
                visited.add(node)
                if node.next:
                    stack.append(node.next)

                if node.child:
                    stack.append(node.child)

        dfs(head)
        if not res:
            return None
        head = res[0]
        res.append(None)
        res.insert(0, None)
        
        for i in range(1, len(res) - 1):
            node = res[i]
            node.child = None
            node.next = res[i+1]
            node.prev = res[i-1]

        return head

