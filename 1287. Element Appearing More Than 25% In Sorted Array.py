Question:
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of 
the time, return that integer.

Example 1:
Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6

Solution:
  def findSpecialInteger(self, arr: List[int]) -> int:
      n = len(arr) // 4
      for i in range(len(arr)):
          if arr[i] == arr[i + n]:
            return arr[i]
