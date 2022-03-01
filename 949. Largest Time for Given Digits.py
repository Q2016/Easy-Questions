Question:
Given an array arr of 4 digits, find the latest 24-hour time that can be made using each digit exactly once.
24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, 
and the latest is 23:59. Return the latest 24-hour time in "HH:MM" format. If no valid time can be made, return an empty string.

Example 1:
Input: arr = [1,2,3,4]
Output: "23:41"
Explanation: The valid 24-hour times are "12:34", "12:43", "13:24", "13:42", "14:23", "14:32", "21:34", "21:43", "23:14", and "23:41". 
Of these times, "23:41" is the latest.


Solution: Use of itertools.permutations
    
There are two conditions that we should meet, in order to construct a valid time format:
HH < 24: The first two digits, i.e. the hour, should be less than 24.
MM < 60: The last two digits, i.e. the minute, should be less than 60.
The algorithm can be implemented in a single loop over all the possible permutations for the given 4 digits.
At each iteration, we check if we could build a valid time based on the conditions we presented before.
Meanwhile, we use a variable (i.e.max_time) to keep track of the maximum valid time that we've seen during the iteration.
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        
        max_time = -1
        # enumerate all possibilities, with the permutation() func
        for h, i, j, k in itertools.permutations(A):
            hour = h*10 + i
            minute = j*10 + k
            if hour < 24 and minute < 60:
                max_time = max(max_time, hour * 60 + minute)
        
        if max_time == -1:
            return ""
        else:
            return "{:02d}:{:02d}".format(max_time // 60, max_time % 60)
