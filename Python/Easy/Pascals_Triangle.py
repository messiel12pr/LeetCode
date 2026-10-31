'''

    118. Pascal's Triangle

'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        if numRows == 2:
            return [[1], [1,1]]

        result_matrix = [[1], [1, 1]]

        for i in range(1, numRows - 1, 1): 
            row = [1]
            for j in range(len(result_matrix[i])-1): 
                row.append(result_matrix[i][j] + result_matrix[i][j+1])

            row.append(1)
            result_matrix.append(row)

        return result_matrix
