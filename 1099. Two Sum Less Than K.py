Question:
Given an array nums of integers and integer k, return the maximum sum such that there exists i < j 
with nums[i] + nums[j] = sum and sum < k. If no i, j exist satisfying this equation, return -1.

Example 1:
Input: nums = [34,23,1,24,75,33,54,8], k = 60
Output: 58
Explanation: We can use 34 and 24 to sum 58 which is less than 60.


    
    
    
    
Solution: Two pointers
Sorted and then use two pointers technique. If sorted then complexity is not O(N)!

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        
        nums = sorted(nums)
        max_sum = -1
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            if nums[left] + nums[right] >= k:
                right -= 1
            else:
                max_sum = max(max_sum, nums[left] + nums[right])
                left += 1
        return max_sum
        
        
Time Complexity: O(N).
Space Complexity: O(1).
