Question:
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Solution:
# this solution is "not" good look at the O(1) solution 


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        n=0
        l=len(nums)
        for i in range(l):
            if nums[i]==0:
                n+=1
        
        i=0

        while i< l:
            if nums[i]==0:

                for j in range(i,l-1):
                    nums[j]=nums[j+1]
            else:
                i+=1

        for i in range(n):
            nums[l-1-i]=0
