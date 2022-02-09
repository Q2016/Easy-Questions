Question:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it 
will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob 
tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Solution:
# https://www.youtube.com/watch?v=73r3KWiEvyk

#f(0) = nums[0]
#f(1) = max(num[0], num[1])
#f(k) = max( f(k-2) + nums[k], f(k-1) )


class Solution:
    
    def rob(self, arr: List[int]) -> int:
        arrLength = len(arr)
        if arrLength == 0: return 0
        elif arrLength == 1: return arr[0]
        elif arrLength == 2: return max(arr[0], arr[1])
        else:
            return max(arr[0] + self.rob(arr[2:]), self.rob(arr[1:]))

