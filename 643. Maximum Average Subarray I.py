Question:
You are given an integer array nums consisting of n elements, and an integer k. Find a contiguous subarray whose length is equal to k that has 
the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75


Solution: Sliding Window
Instead of creating a cumulative sum array first, and then traversing over it to determine the required sum, we can simply traverse 
over numsnums just once, and on the go keep on determining the sums possible for the subarrays of length k. To understand the idea, 
assume that we already know the sum of elements from index i to index i+k, say it is x. Now, to determine the sum of elements from the 
index i+1 to the index i+k+1, all we need to do is to subtract the element nums[i] from x and to add the element nums[i+k+1] to x. We 
can carry out our process based on this idea and determine the maximum possible average.

public class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double sum=0;
        for(int i=0;i<k;i++)
            sum+=nums[i];
        double res=sum;
        for(int i=k;i<nums.length;i++){
            sum+=nums[i]-nums[i-k];
                res=Math.max(res,sum);
        }
        return res/k;
    }
}
