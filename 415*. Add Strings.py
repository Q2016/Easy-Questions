Question:
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert 
the inputs to integers directly.

Example 1:
Input: num1 = "11", num2 = "123"
Output: "134"

  
  
  
  
  
  
  
  
  
  
Solution:  
  
https://www.youtube.com/watch?v=_Qp-CTzat50  
  

class Solution(object):
    def addStrings(self, num1, num2):

        i=len(num1)
        j=len(num2)
      
        num1, num2 = list(num1), list(num2)
        carry=0
        result =[]
        
        while  i>= 0 or j >= 0:
            sum=carry
            if i>=0:
              i-=1
              sum += ord(num1[i])-ord('0')            
            
            if j>=0:
              j-=1
              sum += ord(num2[j])-ord('0') 
 
            result.append(sum % 10)
            carry = sum // 10
    
        if carry !=0: 
          result.append(carry)
          
        return ''.join([str(i) for i in res])[::-1]
