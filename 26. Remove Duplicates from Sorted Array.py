Question:
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. Since it is impossible to change the length of the array in some languages, you must 
instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then 
the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
Return k after placing the final result in the first k slots of nums. Do not allocate extra space for another array. You must do this by modifying 
the input array in-place with O(1) extra memory.

Custom Judge:
The judge will test your solution with the following code:
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length
int k = removeDuplicates(nums); // Calls your implementation
assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Solution:
Given a sorted array and we need to return the length of the unique elements instead of the entire array. There is no need to delete the duplicate elements also.

Since, our first element is already present at index 0 (it is a unique element), we quickly run a for loop for the entire array to scan for unique elements.
If the current element and the next element are the same, then we just keep on going till we find a different element
Once we find a different element, it is inserted at index 1, because, index 0 is taken by the first unique element.
Once this is done, the same scanning is done to find out the next unique element and this element is to be inserted at index 2. This process continues until we are done with unique elements.
We use a variable (x = 1) which is incremented to the next index whenever we find a unique element and we insert this element at its corresponding index.
x = 1
for i in range(len(nums)-1):
	if(nums[i]!=nums[i+1]):
		nums[x] = nums[i+1]
		x+=1
return(x)
