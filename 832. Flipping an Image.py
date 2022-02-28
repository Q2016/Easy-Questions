Question:
Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.
To flip an image horizontally means that each row of the image is reversed.
For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
For example, inverting [0,1,1] results in [1,0,0].

Example 1:
Input: image = [[1,1,0],
                [1,0,1],
                [0,0,0]]
Output: [[1,0,0],
         [0,1,0],
         [1,1,1]]
Explanation: First reverse each row: [[0,1,1],
                                      [1,0,1],
                                      [0,0,0]].
Then, invert the image: [[1,0,0],
                         [0,1,0],
                         [1,1,1]]

    
Solution: Inverse of binary matrix is 1-i per each element i
We can do this in place. In each row, the ith value from the left is equal to the inverse of the ith value from the right.
We use (C+1) / 2 (with floor division) to iterate over all indexes i in the first half of the row, including the center.

    def flipAndInvertImage(self, A):
        return [[1-i for i in row[::-1]] for row in A]
