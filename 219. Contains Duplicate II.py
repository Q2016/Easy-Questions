Question:
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such 
that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Solution:
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        slow,fast=0,1
        
        while slow<len(nums):
            
            while fast<len(nums):
                
                if nums[slow]==nums[fast] and (fast-slow)<=k:
                    return True
                else:
                    fast+=1
            slow+=1
            
        return False
    
    
    # there is a one loop solution using dictionary
