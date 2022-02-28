Question:
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.
Given a row x col grid of integers, how many 3 x 3 "magic square" subgrids are there? 

Example 1:
Input: grid = [[4,3,8,4], Output: 1
               [9,5,1,9],
               [2,7,6,2]]
    
Solution:
class Solution:
    
    # send 3x3 matrix blocks
    def numMagicSquaresInside(self, grid):
        cnt = 0
        # Construct the 3x3 square
        for i in range(len(grid)-2):
            for j in range(len(grid)-2):
                temp_grid = [grid[i+k][j:j+3] for k in range(3)] # pythonic way of sending a block array
                if self.isMagicSquare(temp_grid):
                    cnt += 1
        return cnt
        
    # check for each block if it's magic
    def isMagicSquare(self, grid):
        # Check the elements
        flat = [num for row in grid for num in row]
        if sorted(flat) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return False
        # Check the row, column and diagnal sums
        row_sums = [sum(row) for row in grid]
        col_sums = [sum([row[i] for row in grid]) for i in range(3)]
        diag_sums = [sum([grid[i][i] for i in range(3)]), (grid[0][2] + grid[1][1] + grid[2][0])]
        row_sums.extend(col_sums)
        row_sums.extend(diag_sums)
        return len(set(row_sums)) == 1
