Question:
Given an integer array arr that is guaranteed to be a mountain, return any i such that          /\
arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].            /  \
                                                                                              /    \









Solution: Linear Scan, look at the 'if' condition

    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        for i in range(1, n-1):
            if arr[i-1] < arr[i] > arr[i+1]: # we can use multiple conditions in python
                return i

            
Complexity:
Time: O(N)
Space: O(1)
