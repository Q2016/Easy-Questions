Question:
Given a positive integer num, write a function which returns True if num is a perfect square else False.
Follow up: Do not use any built-in library function such as sqrt.
 
Example 1:
Input: num = 16
Output: true

 
 
 
 
 
 
 
 
 
 
Solution: Binary Search

----> Binary Search Method

   def BinarySearch(self, num):
        left = 0
        right = num
        
        while left <= right:
            mid = left + (right-left)//2
            if  mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                right = mid -1
            else:
                left = mid +1
        return False
 
 
----> Using Newton's Method

   def NewtonMethod(self, num):
        r = num
        while r*r > num:
            r = (r + num/r) // 2
        return r*r == num
 
 
 
Solving with Bitwise trick.

   def BitwiseTrick(self, num):
       root = 0
       bit = 1 << 15
       
       while bit > 0 :
           root |= bit
           if root > num // root:    
               root ^= bit                
           bit >>= 1        
       return root * root == num

      
Math Trick for Square number is 1+3+5+ ... +(2n-1)
   
   def Math(self, num):
        i = 1
        while (num>0):
            num -= i
            i += 2       
        return num == 0

       
Linear Method (Naive) - For comparison
    
   def Linear(self, num):
        i = 1
        while i ** 2 <= num:
            if i ** 2 == num:
                return True
            else:
                i += 1
        return False
