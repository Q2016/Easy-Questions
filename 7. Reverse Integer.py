Question:
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the 
signed 32-bit integer range [-231, 231 - 1], then return 0.

Example 1:
Input: x = 123
Output: 321

    
    
Solution:
    
    def reverse(self, x):
        result = 0
        if x < 0:
            symbol = -1
            x = -x
        else:
            symbol = 1
        while x:
            result = result * 10 + x % 10
            x /= 10
        return 0 if result > pow(2, 31) else result * symbol
