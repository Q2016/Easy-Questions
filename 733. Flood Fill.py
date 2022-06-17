Question:
You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].
To perform a flood fill, start from image[sr][sc] and replace with newColor any pixels connected 4-directionally. 
Return the modified image after performing the flood fill.

Example 1:
Input: image = [[1,1,1],  sr = 1, sc = 1, newColor = 2
                [1,1,0],
                [1,0,1]],
Output: [[2,2,2],
         [2,2,0],
         [2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the 
same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.



Solution: Depth-First Search
We perform the algorithm explained in the problem description: paint the starting pixels, plus adjacent pixels of the same color, and so on.
Say color is the color of the starting pixel. Let's floodfill the starting pixel: we change the color of that pixel to the new color, 
then check the 4 neighboring pixels to make sure they are valid pixels of the same color, and of the valid ones, we floodfill those, and so on.
We can use a function dfs to perform a floodfill on a target pixel.


    def floodFill(self, image, sr, sc, newColor):
        
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r-1, c)
                if r+1 < R: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < C: dfs(r, c+1)
      
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        dfs(sr, sc)
        
        return image
