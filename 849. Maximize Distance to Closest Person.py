Question:
You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 
represents that the ith seat is empty (0-indexed). There is at least one empty seat, and at least one person sitting.
Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 
Return that maximum distance to the closest person.

Example 1:
Input: seats = [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.

Solution:
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        
        ocu=[]
        for i, n in enumerate(seats):
            if n==1:
                ocu.append(i)
        
        tmp=0
        dis=0
        for i in ocu:
            tmp=i-tmp
            dis=max(dis,tmp)
            tmp=i
            
        return dis//2
