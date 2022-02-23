Question:
Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

Example 1:
Input: matrix = [[1,2,3,4],
                 [5,1,2,3],
                 [9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are: "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]". In each diagonal all elements are the same, so the answer is True.

Solution:

    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n=len(matrix[0])
        m=len(matrix)
        d = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                d[i-j].append(matrix[i][j]) 
        for _, t in d.items():
            if len(set(t))!=1:
                return False
        
        return True
