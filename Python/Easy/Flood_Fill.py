'''

    733. Flood Fill

'''

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = [(sr, sc)]
        visited = set()
        visited.add((sr, sc))
        start = image[sr][sc]

        while queue:
            r, c = queue.pop(0)
            if image[r][c] == start:
                image[r][c] = color

            for r2, c2 in [(r, c-1), (r, c+1), (r-1, c), (r+1, c)]:
                if r2 not in range(len(image)) or c2 not in range(len(image[0])) or (r2, c2) in visited:
                    continue

                if image[r2][c2] == start:
                    visited.add((r2, c2))
                    queue.append((r2, c2))

        return image