Question:
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of 
the time, return that integer.

Example 1:
Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6

  
  
  
  
  
  
  
  
  
  
Solution:

The solution for this problem is based on the array being sorted, in the un-sorted array, we need to use 169. Majority Element: Boyer-Moore Majority Vote
  
  def findSpecialInteger(self, arr: List[int]) -> int:
      n = len(arr) // 4
      for i in range(len(arr)):
          if arr[i] == arr[i + n]:
            return arr[i]

          
          
169. Majority Element: Boyer-Moore Majority Vote  
  
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
