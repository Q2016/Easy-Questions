Question:
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.
Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 
should be placed at the end of arr1 in ascending order.

Example 1:
Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

    
    
    
    
    
Solution:
Similar to my solution of 791. Custom Sort String

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans, cnt = [], collections.Counter(arr1)         # Count each number in arr1
        for i in arr2:
            if cnt[i]: ans.extend([i] * cnt.pop(i))      # Sort the common numbers in both arrays by the order of arr2. 
        for i in range(1001):                #|> arrays in arr2 are removed by pop in the line above           
            if cnt[i]: ans.extend([i] * cnt.pop(i))      # Sort the numbers only in arr1.
        return ans
Analysis:

Time: O(max(n2, N)), space: O(n1).
