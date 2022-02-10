Question:
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.
We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

Example 1:
Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.


Solution:
https://leetcode.com/problems/non-decreasing-array/discuss/1190763/JS-Python-Java-C%2B%2B-or-Simple-Solution-w-Visual-Explanation
  
This problem seems easy at first read. If we iterate through the nums array (N), count the number of instances in which an element is lower 
than the one preceeding (err), and then see that count go above 1, then we should be able to return false. The problem becomes more difficult, 
however, once we realize that we're allowed to modify one element, which will naturally impact its relationship with the surrounding elements.
With that in mind, we can think of the different possible scenarios faced when we find an incidence of decreasing value. Consider the base scenario, 
with N[i-1] = a and N[i] = b:
In this base scenario, we can see that there are two ways to fix this decrease, either by decreasing N[i-1] to b or by increasing N[i] to a. 
But which one is better? To answer that, we'll have to observe the surrounding elements (N[i-2] and N[i+1]).
Right away, we can see that there are three possible scenarios for each of the surrounding elements. They can either be larger than a (x >= a), 
in between a and b (b < y < a) or smaller than b (z <= b):
Scenarios XAB and ABZ can quickly be determined to trigger a return of false because in both cases the err count will increment to 2:
Things get more complicated, however, once the values are staggered. In the case of ZABX, we can either move a down or b up in order to achieve 
increasing values, while in YABX we can only move b up and in ZABY we can only move a down:
In the final scenario, YABY, there is no possible way to fix the array with one modification, even though there's only one initial incidence of 
a descending value:
With this all in mind, we can write our function to return false if we see err > 1 or if we see the YABY scenario. If we reach the end without 
triggering either condition, we can return true.

Time Complexity: O(N) where N is the length of N
Space Complexity: O(1) with no modification of inputs


class Solution:
    def checkPossibility(self, N: List[int]) -> bool:
        err = 0
        for i in range(1, len(N)):
            if N[i] < N[i-1]:
                if err or (i > 1 and i < len(N) - 1 and N[i-2] > N[i] and N[i+1] < N[i-1]):
                    return False
                err = 1
        return True
