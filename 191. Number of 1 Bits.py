Question:
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Example 1:
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

 
 
 
 
 
 
 
 
 
Solution:
1.Built in solution with built-in function:

def hammingWeight(self, n):
    return bin(n).count('1')

2.Using bit operation to cancel a 1 in each round
Think of a number in binary n = XXXXXX1000, n - 1 is XXXXXX0111. n & (n - 1) will be XXXXXX0000 which is just remove the last significant 1

def hammingWeight(self, n):
    c = 0
    while n:
        n &= n - 1
        c += 1
    return c
