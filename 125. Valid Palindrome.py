Question:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers. Given a string s, return true if it is a palindrome, 
or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

    
    
    
    
    
    
Solution: Two Pointers
def isPalindrome(self, s):
    l, r = 0, len(s)-1
    while l < r:
        # move the left and right  pointers to sth that you can compare
        while l < r and not s[l].isalnum(): #The isalnum() method returns True if all characters in the string are alphanumeric.
            l += 1
        while l <r and not s[r].isalnum():
            r -= 1
        
        if s[l].lower() != s[r].lower(): # actual test of palindrome is done here
            return False
        
        l +=1; r -= 1
    
    return True
