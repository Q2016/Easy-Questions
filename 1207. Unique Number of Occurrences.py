Question:
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.

Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.


Solution:
Count the occurrences of each char; Compare if the numbers of distinct chars and distinct counts are equal.

    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = collections.Counter(arr)
        return len(c) == len(set(c.values())) 
Analysis:

Time & space: O(n), where n = arr.length
