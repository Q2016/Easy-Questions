Question:
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

Example 1:
Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3. The second distinct maximum is 2. The third distinct maximum is 1.







Solution:

Time is O(n)        
        
class Solution:
    def thirdMax(self, nums):

        n1 = n2 = n3 = None
        for num in nums:
            if n1 == num or n2 == num or n3 == num: continue
            if n1 == None or num > n1:
                n1, n2, n3 = num, n1, n2
            elif n2 == None or num > n2 :
                n2, n3 = num, n2
            elif n3 == None or num > n3:
                n3 = num
        return n3 if n3!=None else n1
