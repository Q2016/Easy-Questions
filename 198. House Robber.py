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


Solution: DP
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

Time Complexity:
If we add memoization like the code below, will be Time O(n) and Space O(n)    

Recursive + memo (top-down):

int[] memo;
public int rob(int[] nums) {
    memo = new int[nums.length + 1];
    Arrays.fill(memo, -1);
    return rob(nums, nums.length - 1);
}

private int rob(int[] nums, int i) {
    if (i < 0) {
        return 0;
    }
    if (memo[i] >= 0) {
        return memo[i];
    }
    int result = Math.max(rob(nums, i - 2) + nums[i], rob(nums, i - 1));
    memo[i] = result;
    return result;
}


Best Solution:

At each house there are two options: either to rob it or not to rob it.

Option 1: If rob, then rob = not_rob + nums[i]
(max money if rob the current house = max money if not rob the last house + amount of the current house)
Option 2: If not rob, then not_rob = max(rob, not_rob)
(max money if not rob the current house = max money at the last house, either rob or not rob)

Varibles: rob = max money if rob the current house
not_rob = max money if not rob the current house.
Both variables are initially set to 0

Complexity:
time = O(n)
Space = O(1)

Here is the code:

class Solution(object):
    def rob(self, nums):
        rob, not_rob = 0, 0
        for num in nums:
            rob, not_rob = not_rob + num, max(rob, not_rob)
        return max(rob, not_rob)
