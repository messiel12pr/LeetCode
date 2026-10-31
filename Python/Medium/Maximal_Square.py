'''

    221. Maximal Square

'''

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), len(matrix[0])
        hm = {}

        def rec(r, c):
            if r >= n or c >= m:
                return 0
            
            if (r, c) not in hm:
                down = rec(r + 1, c)
                right = rec(r, c + 1)
                diagonal = rec(r + 1, c + 1)
                hm[(r, c)] = 0

                if matrix[r][c] == "1":
                    hm[(r, c)] = 1 + min(down, right, diagonal)
            
            return hm[(r, c)]

        rec(0, 0)
        return max(hm.values()) * max(hm.values())
