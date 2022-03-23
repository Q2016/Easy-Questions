Question:
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

Example 1:
Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3. The second distinct maximum is 2. The third distinct maximum is 1.







Solution:

Time is O(n)        
        
    def thirdMax(self, nums):

        n1 = n2 = n3 = None
        for i in nums:
            if n1 == i or n2 == i or n3 == i: # one of the maxes is obtained
                continue 
            if n1 == None or i > n1: # substitute for the first max 
                n1, n2, n3 = i, n1, n2
            elif n2 == None or i > n2 : # substitute for the second max
                n2, n3 = i, n2
            elif n3 == None or i > n3: # substitute for the third max
                n3 = i
        return n3 if n3!=None else n1
