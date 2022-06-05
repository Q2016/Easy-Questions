Question:
Reverse bits of a given 32 bits unsigned integer.

Example 1:
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)




    
    
    
    
    
    
    
    
    
    
Solution: Bits
https://www.youtube.com/watch?v=UcoN6UjAI64

0&1=0 but 1&1=1 by &ing we can discover what value it was
shift to the right 01<<1 => 10 if want to get the ith bit then (n>>i)&1



class Solution:
    def reverseBits(self, n):
        out = 0
        for i in range(32):
            bit=(n>>i)&1 # get the ith bit of n
            res= res | (bit <<(31-i)) # send the ith bit to the end and 'or'it
            # 'or' operation saves the 1's and 0's 

       
       
Compexity: 
Time complexity is O(32), 
Space complexity is O(1).
       
