'''

    994. Rotting Oranges

    i am not proud of this solution lol
'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        times = [[float("inf") for x in range(len(grid[0]))] for y in range(len(grid))]

        def bfs(r, c):
            queue = [(r, c, 1)]
            visited = set()
            visited.add((r, c))

            while queue:
                x, y, i = queue.pop(0)
                
                for x2, y2, i2 in [(x - 1, y, i), (x + 1, y, i), (x, y - 1, i), (x, y + 1, i)]:
                    if x2 not in range(len(grid)) or y2 not in range(len(grid[0])) or (x2, y2) in visited or grid[x2][y2] in (0, 2):
                        continue

                    if times[x2][y2] == float("inf") or times[x2][y2] > i2:
                        times[x2][y2] = i2

                    queue.append((x2, y2, i2 + 1))
                    visited.add((x2, y2))

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 2:
                    bfs(x, y)

        res = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if times[x][y] != float("inf"):
                    res = max(res, times[x][y])

                if times[x][y] == float("inf") and grid[x][y] == 1:
                    return -1

        return res