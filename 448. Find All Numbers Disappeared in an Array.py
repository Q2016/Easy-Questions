Question:
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]



Solution: Index mapping (very smart)
For each number i in nums,
we mark the number that i points as negative.
Then we filter the list, get all the indexes
who points to a positive number.
Since those indexes are not visited.


    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            index = abs(nums[i]) - 1  # map i to index
            nums[index] = - abs(nums[index]) # deemed as existing element
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]  
