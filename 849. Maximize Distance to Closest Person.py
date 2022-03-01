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




Solution: One pass
How to find the max distance between two 1s. 

    def maxDistToClosest(seats) :
        longest = 0 
        beginning = 0 
        i = 0
        # count zeros in beginning
        while (seats[i]==0):
            beginning++
            i++
        # find longest sequence of zeros in middle
        count = beginning
        while i<len(seats):
            if (seats[i] == 0):
                count++
            else:
                longest = max(count, longest)
                count = 0
        # at the end, count = length of zeros in the end
        # in the middle we have to divide the length in two to find maximum distance
        longest = longest/2 if longest % 2 == 0 else longest/2+1
        # return the largest distance
        return max(longest, count, beginning)
    
