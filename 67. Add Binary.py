Question:
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

  
  
  
  
  
  
  
  
  
  
  
Solution:
  
https://www.youtube.com/watch?v=keuWJ47xG8g
  
  
  class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        a=a[::-1]
        b=b[::-1]
        carry = 0
        
        for i in range(max(len(a),len(b))):
            digitA=ord(a[i])-ord("0") if i<len(a) else 0
            digitB=ord(b[i])-ord("0") if i<len(b) else 0
            
            total=digitA+digitB+carry
            char=str(total%2)
            res=char+res
            carry=total//2
            
        if carry : 
          res ="1"+res
          
        return res
