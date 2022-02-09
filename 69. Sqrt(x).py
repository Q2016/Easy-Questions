Question:
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

Solution:

# newton method
# https://en.wikipedia.org/wiki/Integer_square_root#Using_only_integer_division

class Solution:
    def mySqrt(self, s: int) -> int:
        x0 = s 
	
        x1 = ( x0 + s / x0 ) 

        while x1 < x0: 		
            x0 = x1;
            x1 = ( x0 + s / x0 ) 		

        return x0
