Question:
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

 
 
 
 
 
 
 
 
 
Solution: Boyer-Moore Majority Vote
We will be using Boyer-Moore Majority Vote, which will find the majority vote (element found over n/2 times) for us. We must keep a count 
variable and a majority variable which keeps track of the current majority. The idea is to increment the count when we encounter the majority 
and decrement the count when a different value is encountered. This means that if we reach a count value of 0, then no previous number has been 
the majority in the subarray that we have looked at. So, we can set the current element as the majority and continue with our algorithm. At the 
end of the array we will have found an element that is equal to the majority because it exists more times than the rest of the elements combined. 
The question states that we are guarenteed to have a majority, but if we didn't we would have to run through the list another time to make sure it 
is the majority.


from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        majority = 0
        for num in nums:
            if count == 0:
                majority = num
                count += 1
            elif num == majority:
                count += 1
            else:
                count -= 1
        return majority

Complexity
Time is O(n)
Space is O(1)       
