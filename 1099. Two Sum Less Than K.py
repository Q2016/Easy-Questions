Question:
Given an array nums of integers and integer k, return the maximum sum such that there exists i < j 
with nums[i] + nums[j] = sum and sum < k. If no i, j exist satisfying this equation, return -1.

Example 1:
Input: nums = [34,23,1,24,75,33,54,8], k = 60
Output: 58
Explanation: We can use 34 and 24 to sum 58 which is less than 60.


Solution: Two pointers
Sorted and then use two pointers technique.

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        
        nums = sorted(nums)
        i = 0
        j = len(nums) - 1
        
        max_sum = -1
        
        while i < j:
            if nums[i] + nums[j] >= k:
                j -= 1
            else:
                max_sum = max(max_sum, nums[i] + nums[j])
                i += 1
        
        return max_sum
        
        
Time Complexity: O(N).
Space Complexity: O(1).
