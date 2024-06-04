'''
    797. All Paths From Source to Target
'''

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def path(idx, curr):
            if idx == len(graph) - 1:
                res.append(curr) 

            for adj in graph[idx]:
                new_path = curr[:]
                new_path.append(adj)

                if adj == len(graph) - 1:
                    res.append(new_path) 

                else:
                    path(adj, new_path)

        res = []
        for adj in graph[0]:
            curr_path = [0, adj]
            path(adj, curr_path)

        return res