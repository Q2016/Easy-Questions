Question:
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 
Example 1:
Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15

Solution:
Didn't know about the divmod() function until this problem. It's an alternative way to iterate through the digits of an integer. 
By dividing by 10, we iterate backwards through the integer.

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        my_prod = 1
        my_sum = 0
        
        while n:
            n, remainder = divmod(n, 10)
            my_prod *= remainder            
            my_sum += remainder
            
        return my_prod - my_sum
