'''

    74. Search a 2D Matrix

'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_start = 0
        row_end = len(matrix) - 1

        while row_start <= row_end:
            middle = (row_start + row_end)//2

            if target in range(matrix[middle][0], matrix[middle][-1]) or target in (matrix[middle][0], matrix[middle][-1]):
                break

            elif target > matrix[middle][-1]:
                row_start = middle + 1

            else:
                row_end = middle - 1

        l = 0
        r = len(matrix[middle]) - 1

        while l <= r:
            m = (l + r)//2

            if matrix[middle][m] == target:
                return True

            elif matrix[middle][m] > target:
                r = m - 1

            else:
                l = m + 1

        return False