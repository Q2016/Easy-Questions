Question:
You are given n points in the plane that are all distinct, where points[i] = [xi, yi]. A boomerang is a tuple of 
points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).
Return the number of boomerangs.

Example 1:
Input: points = [[0,0],[1,0],[2,0]]
Output: 2
Explanation: The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]].

Solution:
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def sub_lists(l,m):
            lists = [[]]
            for i in range(len(l) + 1):
                for j in range(i):
                    lists.append(l[j: i])
            return [p for p in lists if len(p)==m]

        if len(points)<3:
            return 0

        p=points.copy()

        n=0
        for i in points:
            p.remove(i)

            p_list=sub_lists(p,2)
            #print(p_list)
            for pp in p_list:
                if (i[0]-pp[0][0])**2+(i[1]-pp[0][1])**2==(i[0]-pp[1][0])**2+(i[1]-pp[1][1])**2:
                    n+=1
            p.append(i)
        return n*2
