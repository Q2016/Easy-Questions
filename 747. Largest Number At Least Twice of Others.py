Question:
You are given an integer array nums where the largest integer is unique. Determine whether the largest element in the array is at least 
twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.

Example 1:
Input: nums = [3,6,1,0]
Output: 1
Explanation: 6 is the largest integer. For every other number in the array x, 6 is at least twice as big as x. The index of value 6 is 1, so we return 1.






Solution: Trick: save highest and second highest
The question says "whether the largest element in the array is at least 
twice as much as every other number in the array" that's why we need the second highest               
        
Just iterate through the array and note the highest and second highest numbers. Might as well take note of the index at the same time.
One slightly clever idea was to shuffle the highest to the second-highest whenever a new highest was found. That was a way to handle the 
case where there are two (or more) value tied for highest.

class Solution:
    def dominantIndex(self, nums):
        if len(nums) == 0: return -1

        highest = -1
        secondHighest = -1
        highestIndex = 0
        
        for i,n in enumerate(nums):
            if n >= highest:
                secondHighest = highest
                highest = n
                highestIndex = i
            elif n > secondHighest:
                secondHighest = n

        if highest < secondHighest*2:
            highestIndex = -1
        
        return highestIndex
