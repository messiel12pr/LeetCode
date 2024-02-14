'''

    200. Number of Islands

    Solution

'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        len_rows = len(grid)
        len_cols = len(grid[0])
        visited = set()
        res = 0

        def dfs(r, c):
            if (r) not in range(len_rows) or (c) not in range(len_cols) or grid[r][c] == "0" or (r, c) in visited:
                return

            if grid[r][c] == "1":
                grid[r][c] = "0"
            
            visited.add((r, c))

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        for row in range(len_rows):
            for col in range(len_cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    res += 1
                    dfs(row, col)
    
        return res