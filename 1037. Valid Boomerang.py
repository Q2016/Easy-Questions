Question:
Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.
A boomerang is a set of three points that are all distinct and not in a straight line.

Example 1:
Input: points = [[1,1],[2,3],[3,2]]
Output: true


Solution:
If the 3 points can form a triangle ABC, then the slopes of any 2 edges, such as AB and AC, are not equal.

Use Formula as follows:

(y0 - y1) / (x0 - x1) != (y0 - y2) / (x0 - x2) =>

(x0 - x2) * (y0 - y1) != (x0 - x1) * (y0 - y2)

Where
A:
x0 = p[0][0]
y0 = p[0][1]
B:
x1 = p[1][0]
y1 = p[1][1]
C:
x2 = p[2][0]
y2 = p[2][1]

Use the muliplication form to cover corner cases such as, a slope is infinity, 2 or 3 points are equal.

    def isBoomerang(self, p: List[List[int]]) -> bool:
        return (p[0][0] - p[2][0]) * (p[0][1] - p[1][1]) != (p[0][0] - p[1][0]) * (p[0][1] - p[2][1])
