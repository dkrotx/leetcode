class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0]*n for _ in range(n)]
        row, col = 0, 0
        num = 1
        d = 0

        while True:
            if col >= n - d:
                break
            while col < n - d:
                matrix[row][col] = num
                col += 1
                num += 1

            row += 1; col = n - 1 - d
            if row >= n - d:
                break
            while row < n - d:
                matrix[row][col] = num
                num += 1
                row += 1

            col -= 1; row = n - 1 - d
            if col < d:
                break
            while col >= d:
                matrix[row][col] = num
                num += 1
                col -= 1

            row -= 1; col = d
            if row <= d:
                break
            while row > d:
                matrix[row][col] = num
                num += 1
                row -= 1

            # moving to next loop
            d += 1
            row = d; col += 1

        return matrix
