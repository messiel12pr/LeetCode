'''

    133. Clone Graph

'''

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node:
            visited = set()
            visited.add(node.val)
            queue = [node]
            adj = {1: Node(1)}

            while queue:
                next_node = queue.pop(0)

                for neighboor in next_node.neighbors:
                    if neighboor.val not in adj:
                        queue.append(neighboor)
                        adj[neighboor.val] = Node(neighboor.val)

                    adj[next_node.val].neighbors.append(adj[neighboor.val])

            return adj[1]