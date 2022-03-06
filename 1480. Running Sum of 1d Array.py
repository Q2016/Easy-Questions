Question:
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

		
		
		
		
		
		
		
Solution: One pass
Time complexity for both the solutions: O(n).
Space complexity in both the solutions: O(n) because we are creating a result list of size n.

Solution 1:

def runningSum(self, nums: List[int]) -> List[int]:
	result = []
	total = 0
	for i in range(len(nums)):
		total += nums[i]
		result.append(total)
	return result
Solution 2: Without using 'total' variable. Just use the last value in result to calculate new sum.

def runningSum(self, nums: List[int]) -> List[int]:
	result = []
	result.append(nums[0])
	for i in range(1, len(nums)):
		result.append(result[-1]+nums[i])
	return result
