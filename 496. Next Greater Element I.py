Question:
The next greater element of some element x in an array, is the first greater element that is to the right of x in the same array.
You are given two arrays nums1 and nums2, where nums1 is a subset of nums2.
For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. 
If there is no next greater element, then the answer for this query is -1. Return an array ans of length nums1.length such that ans[i] is the next 
greater element as described above.

Follow up: Could you find an O(nums1.length+nums2.length) solution?

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.





Solution: (Question is complicated look at the example!, new technique)

https://www.youtube.com/watch?v=68a1Dc_qVq4	
	
Basically the problem says, if in nums1 we are working on 4, then in nums2 first find where is 4 and from that index find the next number 
greater than 4 in nums2. We can see that the solution is always coming from the reverse side of the list nums2. This should tell us to use stack.
We traverse nums2 and start storing elements on the top of stack. If current number is greater than the top of the stack, then we found a pair. 
Keep popping from stack till the top of stack is smaller than current number. After matching pairs are found, push current number on top of stack.
Eventually when there are no more elements in nums2 to traverse, but there are elements in stack, we can justify that next bigger element wasn't 
found for them. Hence we'll put -1 for the remaining elements in stack.


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

	nums1Idx={n:i for i,n in enumerate(nums1)}
	res=[-1]*len(nums1)
	
	for i in range(len(nums2)):
		if nums2[i] not in nums1Idx:
			continue
		for j in range(i+1, len(nums2)):
			if nums2[j]>nums2[i]:
				idx=nums1Idx[nums2[i]]
				res[idx]=nums2[j]
				break
				
	return res
	
	

Time O(m*n)
Space O(m)

Monotonic stack technique

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
	nums1Idx={n:i for i,n in enumerate(nums1)}
	res=[-1]*len(nums1)
	
	stack=[]
	for i in range(len(nums2)):
		cur=num2[i]
		while stack and cur>stack[-1]:
			val=stack.pop()
			idx=num1Idx[val]
			res[idx]=cur
		if cur in num1Idx:
			stack.append(cur)
		
Time O(m+n)
Space O(m)
