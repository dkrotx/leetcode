class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for level in range(len(matrix) // 2):
            for base_column in range(level, len(matrix) - level - 1):
                row = level
                col = base_column
                val = matrix[row][col]
                for side in range(4):
                    new_row = col
                    new_col = len(matrix) - 1 - row
                    val, matrix[new_row][new_col] = matrix[new_row][new_col], val
                    row, col = new_row, new_col
