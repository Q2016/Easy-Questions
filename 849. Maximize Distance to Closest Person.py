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




Solution: Approach #1: Next Array [Accepted]
Intuition

Let left[i] be the distance from seat i to the closest person sitting to the left of i. Similarly, let right[i] be the distance to 
the closest person sitting to the right of i. This is motivated by the idea that the closest person in seat i sits a distance 
min(left[i], right[i]) away.

Algorithm

To construct left[i], notice it is either left[i-1] + 1 if the seat is empty, or 0 if it is full. right[i] is constructed in a similar way.
    
class Solution(object):
    def maxDistToClosest(self, seats):
        N = len(seats)
        left, right = [N] * N, [N] * N

        for i in xrange(N):
            if seats[i] == 1: left[i] = 0
            elif i > 0: left[i] = left[i-1] + 1

        for i in xrange(N-1, -1, -1):
            if seats[i] == 1: right[i] = 0
            elif i < N-1: right[i] = right[i+1] + 1

        return max(min(left[i], right[i])
                   for i, seat in enumerate(seats) if not seat)
    
    
Complexity Analysis

Time Complexity: O(N), where N is the length of seats.

Space Complexity: O(N), the space used by left and right. 
    

Approach #2: Two Pointer [Accepted]
Intuition

As we iterate through seats, we'll update the closest person sitting to our left, and closest person sitting to our right.

Algorithm

Keep track of prev, the filled seat at or to the left of i, and future, the filled seat at or to the right of i.

Then at seat i, the closest person is min(i - prev, future - i), with one exception. i - prev should be considered infinite 
if there is no person to the left of seat i, and similarly future - i is infinite if there is no one to the right of seat i.    


class Solution(object):
    def maxDistToClosest(self, seats):
        people = (i for i, seat in enumerate(seats) if seat)
        prev, future = None, next(people)

        ans = 0
        for i, seat in enumerate(seats):
            if seat:
                prev = i
            else:
                while future is not None and future < i:
                    future = next(people, None)

                left = float('inf') if prev is None else i - prev
                right = float('inf') if future is None else future - i
                ans = max(ans, min(left, right))

        return ans
