Question:
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.
Given a row x col grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).


Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m=grid[0]#col
        n=grid#row
        
        def findRows(grid: List[List[int])-> int:
                   
                                
        def findCols(grid: List[List[int])-> int:
                                
        def findDiag(grid: List[List[int])-> int:
        
        def findADiag(grid: List[List[int])-> int:
        
        
        cnt=0
        for i in range(m-3):
            for j in range(n-3):
                flag=False
                                 
                tmp=grid[j:j+3][i:i+3]# row, col
                a1=findRows(tmp)
                a2=findCols(tmp)
                a3=findDiag(tmp)
                a4=findADiag(tmp)
                
                if a1==a2 and a2==a3 and a3==a4:
                    flag=True
                                 
                if flag==True:
                    cnt+=1
                                 
        return cnt
