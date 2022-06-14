Question:
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
Can be solved in Time/space O(n).

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].





Solution: Two pointers
    
    https://www.youtube.com/watch?v=FPCZsG_AkUg
        
    - Find the lowest element and use it as the center
    - Use right and left lements of this element as right and left pointers 
    - scroll away from the center in both directions as you compare the abs() of left/right elements

    Alternatively, 
        we can assign pointers to both ends of the array as below
    
    
def sortedSquares(self, nums):
    res=[]
    l, r = 0, len(nums) - 1
    while l <= r:
        
        if nums[l]*nums[l] > nums[r]*nums[r]:
            res.append(nums[l]*nums[l])
            l += 1
        else:
            res.appendleft(nums[r]*nums[r])
            r -= 1
    return res[::-1] # reverse



