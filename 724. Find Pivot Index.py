Question:
Given an array of integers nums, calculate the pivot index of this array. The pivot index is the index where the sum of all the numbers strictly to 
the left of the index is equal to the sum of all the numbers strictly to the index's right. 

Example 1:
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11




Solution: Prefix sum

We need to quickly compute the sum of values to the left and the right of every index. Let's say we knew S as the sum of the numbers, 
and we are at index i. If we knew the sum of numbers leftsum that are to the left of index i, then the other sum to the right of the 
index would just be S - nums[i] - leftsum. As such, we only need to know about leftsum to check whether an index is a pivot index in 
constant time. Let's do that: as we iterate through candidate indexes i, we will maintain the correct value of leftsum.


    def pivotIndex(self, nums):
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1
