Question:
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

Example 1:
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

        
        
        
        
        
Solution: Two pass
Find number of zeros and then shift

If we know the number of elements which would be discarded from the end of the array, we can copy the rest. How do we find out how many 
elements would be discarded in the end? The number would be equal to the number of extra zeros which would be added to the array. The extra 
zero would create space for itself by pushing out an element from the end of the array.
Once we know how many elements from the original array would be part of the final array, we can just start copying from the end. Copying from 
the end ensures we don't lose any element since, the last few extraneous elements can be overwritten.

Start from the back and adjust items to correct locations. If item is zero then duplicate it.

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        zeroes = arr.count(0)
        n = len(arr)
        for i in range(n-1, -1, -1):
            if i + zeroes < n:
                arr[i + zeroes] = arr[i]
            if arr[i] == 0: 
                zeroes -= 1
                if i + zeroes < n:
                    arr[i + zeroes] = 0
