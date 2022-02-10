Question:
Given an integer x, return true if x is palindrome integer.An integer is a palindrome when it reads the same backward as forward. 
For example, 121 is a palindrome while 123 is not.
 
Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.


Solution:
This is the easiest way to check if integer is palindrome.

Convert the number to string and compare it with the reversed string.

I wrote this working solution first and then found in the description that we need to solve this problem without converting the input to string. Then I wrote solution 2.

def isPalindrome(self, x: int) -> bool:
	if x < 0:
		return False
	
	return str(x) == str(x)[::-1]
