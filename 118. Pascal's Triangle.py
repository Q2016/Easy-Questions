Question:
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Solution:
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        my_list=[ [1]*numRows for i in range(numRows)]
        
        for i in range(3,numRows):
            for j in range(1,i):
                my_list[i][j]=my_list[i-1][j]+my_list[i][j-1]
                
        return my_list
