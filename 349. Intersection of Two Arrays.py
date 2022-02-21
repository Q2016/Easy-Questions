Question:
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and 
you may return the result in any order.


Solution:

The naive approach would be to iterate along the first array nums1 and to check for each value if this value in nums2 or not. 
If yes - add the value to output. Such an approach would result in a pretty bad O(n×m) time complexity, 
where n and m are arrays' lengths.

class Solution:
    def set_intersection(self, set1, set2):
        return [x for x in set1 if x in set2]
        
    def intersection(self, nums1, nums2):

        set1 = set(nums1)
        set2 = set(nums2)
        
        if len(set1) < len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set2, set1)
