Question:
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 
Example 1:
Input: nums = [3,2,3]
Output: 3

Solution:
//Recursively find the majority in the two halves of nums and combine the results. The base case is that the majority element of a single-element array is just that element.

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        return majority(nums, 0, nums.size() - 1);
    }
private:
    
    int majority(vector<int>& nums, int l, int r) {
        
        if (l == r) {
            return nums[l];
        }
        
        int m,lm,rm;
        
        m = l + (r - l) / 2; 
        lm = majority(nums, l, m); 
        rm = majority(nums, m + 1, r);

        if (lm == rm) {
            return lm;
        }
return count(nums.begin() + l, nums.begin() + r + 1, lm) > count(nums.begin() + l, nums.begin() + r + 1, rm) ? lm : rm;
    }
}; 
