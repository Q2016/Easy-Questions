Question:
Given an integer num, return a string of its base 7 representation.

Example 1:
Input: num = 100
Output: "202"


Solution:
Explanation below code snippet - hope this helps!

If you are confused about the conversion process from base 10 (numbers we are used to) to base 7 read this:

https://runestone.academy/runestone/books/published/pythonds/BasicDS/ConvertingDecimalNumberstoBinaryNumbers.html

class Solution:
    def convertToBase7(self, num: int) -> str:
        
        if not num:
            return '0'
        
        sign = num < 0
        num = abs(num)
        
        stack = []
        while num:
            stack.append(str(num % 7))
            num = num // 7
        
        return '-'*sign + ''.join(stack[::-1])
The first two lines simply handle the edge case that num is zero.

Next, we check to see if num is negative, if it is, lets make it positive using abs, but remember that it was negative with the variable sign. 
(We will take the original sign of the number into account in the return statement.)
Next, iteratively divide num by 7 and at each iteration, keep track of the remainder in a stack. These remainders are the digits that will go into our 
result. However, they are in the reverse order of what we need. Once num equals zero, the while loop will break. Join all of the elements in the stack 
together in reverse order, and add the sign back in. If the number was positive, then sign = False and "-" * False = "" so the negative sign will not 
be included in the result. Side note: The list we use to store the digits was named stack because using:

while stack:
	res += stack.pop()
would achieve the same outcome as ''.join(stack[::-1])
