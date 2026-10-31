'''

    695. Max Area of Island

'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
            scan and find a island
            verify if we havent visited that island
            verify how big is the island
        '''
        # stores a position in the matrix as a tuple
        max_area = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r: int, c: int) -> int: # O(r * c)
            if (r) in range(rows) and (c) in range(cols) and grid[r][c] == 0:
                return 0

            if (r) in range(rows) and (c) in range(cols) and grid[r][c] == 1:
                total = 1
                grid[r][c] = -1

                total += dfs(r + 1, c)
                total += dfs(r - 1, c)
                total += dfs(r, c + 1)
                total += dfs(r, c - 1)

                return total

            return 0

        for r in range(rows): # O(r * c)
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area
