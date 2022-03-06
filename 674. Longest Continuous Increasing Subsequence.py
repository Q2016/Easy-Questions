Question:
Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence. 

Example 1:
Input: nums = [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3. Even though [1,3,5,7] is an increasing subsequence, it is not 
continuous as elements 5 and 7 are separated by element 4.





Solution: Two pointers

    def findLengthOfLCIS(self, nums):
        if not nums:
            return 0
        left = 0
        n = 1
        for right in range(1, len(nums)):
            if nums[right-1] < nums[right]:
                n = max(n, right - left + 1)
            else:
                left = right
        return n    
    
    
Sliding Window:

    def findLengthOfLCIS(self, nums):
        ans = anchor = 0
        for i in range(len(nums)):
            if i and nums[i-1] >= nums[i]: anchor = i
            ans = max(ans, i - anchor + 1)
        return ans
