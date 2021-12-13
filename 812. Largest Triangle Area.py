Explanaiton
Burete force loop on all combinations of three points and calculate the area of these three points.
If you google "three pointes triangle area formula", you can find the answer with the first result in second.

Time complexity
O(N^3) solution, but N <= 50, so it's fast enough.
You may find convex hull first as @weidairpi replies. It help improve to O(M^3 + NlogN) in the best case where M is the number of points on the hull.
But it make this easy problem complex and it stays same complexity in the worst case.








https://leetcode.com/problems/largest-triangle-area/discuss/122711/C%2B%2BJavaPython-Solution-with-Explanation-and-Prove
def largestTriangleArea(self, p):
  for i, j, k in itertools.combinations(p, 3))
    return max(0.5 * abs(i[0] * j[1] + j[0] * k[1] + k[0] * i[1]- j[0] * i[1] - k[0] * j[1] - i[0] * k[1])
            
