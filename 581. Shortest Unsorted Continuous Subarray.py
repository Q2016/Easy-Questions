Question:
Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, 
then the whole array will be sorted in ascending order. Return the shortest such subarray and output its length.

Example 1:
Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.


Solution: Two pointers
First, we have two pointer that finds first non-ascending, l, and first non-descending, r in array.
First if statement checks if l is greater than r which means the array is already sorted.
Now, second set of while loop is for any numbers outside of violating zone that should be included.
Such as following example that would not get caught by first pass:

[1, 3, 7, 2, 5, 4, 6, 10] : left would catch at value 7, index: 2 and right would catch at value 4, index: 5

But, looking at the array the function should also include 3 and 6. And this is why we do another round of while loop.
Instead incrementing and decrementing respective, l and r, we decrement and increment respective l and r.
Thinking about it as adjusting lower bound and upper bound is better.
This adjustment depends on two things: Minimum and maximum values of array nums[l:r+1].
Now, we decrement l value until we find something that is lower than minimum.
Also, we increment r value until we find something that is greater than maximum.
After all that you just need to do l + r - 1.

Analysis:
At worst case, nums is already sorted: O(2n) = O(n)
At worst case, nums is not sorted bound begins in the middle and two values are min and max of entire array: O(2n) = O(n)
Space complexity: Using only 5 variables and it is constant: O(5) = O(1)

    def findUnsortedSubarray(self, nums):

        if len(nums) < 2: return 0
        l, r = 0, len(nums) - 1
        while l < len(nums) - 1 and nums[l] <= nums[l + 1]:
            l += 1
        while r > 0 and nums[r] >= nums[r -1]:
            r -= 1
        if l > r:
            return 0
        temp = nums[l:r+1]
        tempMin = min(temp)
        tempMax = max(temp)
        while l > 0 and tempMin < nums[l-1]:
            l -= 1
        while r < len(nums) - 1 and tempMax > nums[r+1]:
            r += 1
          
        return r - l + 1
