Question:
Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

Example 1:
Input: s = "Hello"
Output: "hello"

    
    
    
    
    
    
    
    
  




Solution:
    
class Solution:
    def toLowerCase(self, str): 
        return "".join(chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in str)

class Solution:
    def toLowerCase(self, str): 
        return "".join(chr(ord(c) + 32) if "A" <= c <= "Z" else c for c in str)

