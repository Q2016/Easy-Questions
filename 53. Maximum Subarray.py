Question:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

    
    
    
    
    
    

    
Solution: Kadane's algorithm
# https://www.youtube.com/watch?v=5WZl3MMT0Eg

The thought follows a simple rule:
If the sum of a subarray is positive, it has possible to make the next value bigger, so we keep do it until it turn to negative.
If the sum is negative, it has no use to the next element, so we break.
it is a game of sum, not the elements.


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub=nums[0]
        curSum=0
        
        for n in nums:
            if curSum<0: # it's assuming the max contiguous subarray can be negative!
                curSum=0
            curSum+=n
            maxSub=max(maxSub, curSum)
        return maxSub

    
    
Time O(n)
Space O(1)
