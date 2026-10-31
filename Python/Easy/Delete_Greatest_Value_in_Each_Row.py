'''

    2500. Delete Greatest Value in Each Row

'''

class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        sorted_grid = []
        res = 0

        for row in grid:
            sorted_grid.append(sorted(row, reverse=True))

        for col in range(len(grid[0])):
            col_max = 0
            for row in range(len(grid)):
                col_max = max(col_max, sorted_grid[row][col])
            res += col_max

        return res
