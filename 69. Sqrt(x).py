Question:
Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.

    
    
    
    
    
    
    
Solution: BST from 278

# newton method
# https://en.wikipedia.org/wiki/Integer_square_root#Using_only_integer_division

Quite an easy problem. We need to search for maximal k satisfying k^2 <= x, so we can easily come up with the solution:

def mySqrt(x: int) -> int:
    left, right = 0, x
    while left < right:
        mid = left + (right - left) // 2
        if mid * mid <= x:
            left = mid + 1
        else:
            right = mid
    return left - 1

There's one thing I'd like to point out. Remember I say that we usually look for the minimal k value satisfying certain condition? 
But in this problem we are searching for maximal k value instead. Feeling confused? Don't be. Actually, the maximal k satisfying 
condition(k) is False is just equal to the minimal k satisfying condition(k) is True minus one. This is why I mentioned earlier 
that we need to decide which value to return, left or left - 1.
