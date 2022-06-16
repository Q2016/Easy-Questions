Question:
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place with O(1) extra memory such that each unique element 
appears only once. 
The relative order of the elements should be kept the same. 
Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums.

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).










Solution:

def removeDuplicates(nums):	
	x = 1
	for i in range(len(nums)-1):
		if(nums[i]!=nums[i+1]):
			nums[x] = nums[i+1]
			x+=1
	return nums
