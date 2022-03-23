Question:
Given an array of integers arr, return true if and only if it is a valid mountain array.
Recall that arr is a mountain array if and only if:
arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]








Solution:One Pass (This is question 852 i.e. repetitative)

If we walk along the mountain from left to right, we have to move strictly up, then strictly down.
Algorithm
Let's walk up from left to right until we can't: that has to be the peak. We should ensure the peak is not the first or last element. 
Then, we walk down. If we reach the end, the array is valid, otherwise its not.


class Solution(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0
        # walk up
        while i+1 < N and A[i] < A[i+1]:
            i += 1
        # peak can't be first or last
        if i == 0 or i == N-1:
            return False
        # walk down
        while i+1 < N and A[i] > A[i+1]:
            i += 1
        return i == N-1
    
Similar question is 852. Peak Index in a Mountain Array:

    Linear Scan, look at the 'if' condition

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        for i in range(1, n-1):
            if arr[i-1] < arr[i] > arr[i+1]: # we can use multiple conditions in python
                return i

            
Complexity:
Time: O(N)
Space: O(1)
    
