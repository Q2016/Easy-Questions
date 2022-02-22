Question:
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. 
If there is no next greater element, then the answer for this query is -1. Return an array ans of length nums1.length such that ans[i] is the next 
greater element as described above.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.


Solution:
Basically the problem says, if in nums1 we are working on 4, then in nums2 first find where is 4 and from that index find the next number 
greater than 4 in nums2. We can see that the solution is always coming from the reverse side of the list nums2. This should tell us to use stack.
We traverse nums2 and start storing elements on the top of stack. If current number is greater than the top of the stack, then we found a pair. 
Keep popping from stack till the top of stack is smaller than current number. After matching pairs are found, push current number on top of stack.
Eventually when there are no more elements in nums2 to traverse, but there are elements in stack, we can justify that next bigger element wasn't 
found for them. Hence we'll put -1 for the remaining elements in stack.


def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
	if not nums2:
		return None
	mapping = {}
	result = []
	stack = []
	stack.append(nums2[0])

	for i in range(1, len(nums2)):
		while stack and nums2[i] > stack[-1]: # if stack is not empty, then compare it's last element with nums2[i]
			mapping[stack[-1]] = nums2[i] # if the new element is greater than stack's top element, then add this to dictionary 
			stack.pop()                   # since we found a pair for the top element, remove it.
		stack.append(nums2[i])                # add the element nums2[i] to the stack because we need to find a number greater than this

	for element in stack:                         # if there are elements in the stack for which we didn't find a greater number, map them to -1
		mapping[element] = -1

	for i in range(len(nums1)):
		result.append(mapping[nums1[i]])
	return result
