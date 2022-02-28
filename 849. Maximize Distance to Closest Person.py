Question:
You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 
represents that the ith seat is empty. There is at least one empty seat, and at least one person sitting. Alex wants to sit in the seat such that 
the distance between him and the closest person to him is maximized. Return that maximum distance to the closest person.

Example 1:
Input: seats = [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.




Solution:
Here we have 4 main cases that need to cover:
[1,0,0,0,1,0] -> 2 -> between ones
[0,0,0,0,0,1] -> 5 -> one in end
[1,0,0,0,0,0] -> 5 -> one in beggining
[0,0,1,0,0,0] -> 3 -> one in middle
Intuition:
Let's have 2 pointers(prev and cur) for keep track ones:
Always move current pointer to right:
[1,0,0,0,1,0]
 p
 c
Till meet next one:
[1,0,0,0,1,0]
 p
         c
Then need to check if we're between 2 ones (seats[prev] == 1):
if yes, then maximize the result with (c - p) // 2      -> cover case #1
if no, then maximize the result with (c - p)            -> cover case #2
finally move prev to cur
But cases 3 and 4 are not covered :(
if seats[prev] points to one:
[0,0,1,0,0,0]
     p
             c
So, let's have a check in the end, like:
if seats[prev] == 1 then let's maximize the result with len(seats) - 1 - prev -> cover cases #3 and #4
Code:

    def maxDistToClosest(self, seats: List[int]) -> int:
        prev, max_len = 0, 0
        for cur, seat in enumerate(seats):
            if seat:
                if seats[prev]:
                    max_len = max(max_len, (cur - prev) // 2)
                else:
                    max_len = max(max_len, (cur - prev))
                prev = cur 
        if seats[prev]: 
            max_len = max(max_len, len(seats) - 1 - prev)     
        return max_len
