from copy import deepcopy
import unittest

class EasySolution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.

        runtime: O(m*n), memory: O(m+n)
        """
        rows = set()
        cols = set()
        
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)
                    
        for r in rows:
            for c in range(len(matrix[r])):
                matrix[r][c] = 0
                
        for c in cols:
            for r in range(len(matrix)):
                matrix[r][c] = 0


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.

        runtime: O(m*n), memory: O(1)
        """
        def set_row_zero(row):
            for column in range(len(matrix[row])):
                matrix[row][column] = 0

        def set_column_zero(column):
            for row in range(len(matrix)):
                matrix[row][column] = 0

        mem_row = None
        mem_col = None
        
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == 0:
                    if mem_row is None:
                        mem_row, mem_col = r, c
                    else:
                        matrix[mem_row][c] = 0
                        matrix[r][mem_col] = 0
        
        if mem_row is None: # no any zeroes
            return

        """ 
        finish setting row and column with zeroes 
        following memorized "mask"
        """
        for c in range(len(matrix[mem_row])):
            if matrix[mem_row][c] == 0 and c != mem_col:
                set_column_zero(c)

            matrix[mem_row][c] = 0
        
        for r in range(len(matrix)):
            if matrix[r][mem_col] == 0 and r != mem_row:
                set_row_zero(r)

            matrix[r][mem_col] = 0
        


class Test(unittest.TestCase):
    def test_simple(self):
        def check(matrix):
            correct = deepcopy(matrix)
            EasySolution().setZeroes(correct)
            Solution().setZeroes(matrix)

            self.assertEqual(correct, matrix)

        check([[0]])
        check([[1, 2], [0, 3]])
        check([[1, 2, 3], [0, 5, 6], [7, 0, 9]])
        check([[0, 2, 3], [4, 0, 6], [7, 8, 0]])


unittest.main()
