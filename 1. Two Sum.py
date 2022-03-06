Question:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].



Solution: Hashmap
Map the diff to each index
# https://www.youtube.com/watch?v=KLlXCFG5TnA
# you can't solve it using two pointer or slidding window
# my own solution with the hint of hashmap

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i, n in enumerate(nums):
            diff=target-n
            if n in d:
                return[i, d[n]]
            d[diff]=i  
