'''

    463. Island Perimeter

'''

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        # Store coordinates as tuples
        visited = set()

        def bfs(r, c) -> int:
            queue = [(r, c)]
            directions = [[0, 1],[0, -1],[1, 0],[-1, 0]]
            total_perimeter = 0

            while queue:
                curr_r, curr_c = queue.pop(0)
                adj_count = 0

                if grid[curr_r][curr_c] == 1 and (curr_r, curr_c) not in visited:
                    visited.add((curr_r, curr_c))
                    for dr, dc in directions:
                        adj_r = curr_r + dr
                        adj_c = curr_c + dc
                        
                        if (adj_r) in range(rows) and (adj_c) in range(cols) and grid[adj_r][adj_c] == 1:
                            queue.append((adj_r, adj_c))
                            adj_count += 1

                    total_perimeter += 4 - adj_count

            return total_perimeter

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return bfs(r, c)
                    
        return 0
