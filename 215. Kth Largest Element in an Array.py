Question:
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
  

  
  
  
  
Solution:

Pyhton:
    def findKthLargest(self, nums, k):
        return sorted(nums, reverse = True)[k-1]  
  

C++:  
  
STL
This problem needs to use partial sorting. In STL, there are two built-in functions (nth_element and partial_sort) for this.

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        nth_element(nums.begin(), nums.begin() + k - 1, nums.end(), greater<int>());
        return nums[k - 1];
    }
};  
  

min-heap using priority_queue

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> pq;
        for (int num : nums) {
            pq.push(num);
            if (pq.size() > k) {
                pq.pop();
            }
        }
        return pq.top();
    }
};

  
  
  
