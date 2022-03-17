Question:
Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be 
formed by any three different points. Answers within 10-5 of the actual answer will be accepted.

Example 1:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2.00000
Explanation: The five points are shown in the above figure. The red triangle is the largest.

	
	
	
	
Solution:
Shoelace Method:

class Solution:
    def largestTriangleArea(self, p: List[List[int]]) -> float:
        L, A = len(p), 0
        for i in range(L-2): # we can replace these loops with itertools.Permutations()
        	for j in range(i+1,L-1):
        		for k in range(j+1,L):
        			R = Area_Shoelace(p[i],p[j],p[k])
        			A = max(A,R)
        return A

def Area_Shoelace(a,b,c): # it's just calculating area, not a big deal
	return abs(a[0]*b[1]+b[0]*c[1]+c[0]*a[1]-(a[0]*c[1]+c[0]*b[1]+b[0]*a[1]))/2
	

Heron's Formula:

class Solution:
    def largestTriangleArea(self, p: List[List[int]]) -> float:
        L, A = len(p), 0
        for i in range(L-2):
        	for j in range(i+1,L-1):
        		for k in range(j+1,L):
        			R = Area_Heron(p[i],p[j],p[k])
        			A = max(A,R)
        return A

def Area_Heron(r,s,t):
	a, b, c = math.hypot(r[0]-s[0],r[1]-s[1]), math.hypot(r[0]-t[0],r[1]-t[1]), math.hypot(s[0]-t[0],s[1]-t[1])
	s = (a + b + c)/2
	return (max(0,s*(s-a)*(s-b)*(s-c)))**.5
