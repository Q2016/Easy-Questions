Question:
Reverse bits of a given 32 bits unsigned integer.

Example 1:
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which 
its binary representation is 00111001011110000010100101000000.



Solution: Bits
We are asked to reverse bits in our number. What is the most logical way to do it? Create number out, process original number bit by bit from end and 
add this bit to the end of our out number, and that is all! Why it is works?

out = (out << 1)^(n & 1) adds last bit of n to out
n >>= 1 removes last bit from n.
Imagine number n = 11011010, and out = 0

out = 0, n = 1101101
out = 01, n = 110110
out = 010, n = 11011
out = 0101, n = 1101
out = 01011, n = 110
out = 010110, n = 11
out = 0101101, n = 1
out = 01011011, n = 0

class Solution:
    def reverseBits(self, n):
        out = 0
        for i in range(32):
            out = (out << 1)^(n & 1)
            n >>= 1
        return out

       
       
Compexity: 
Time complexity is O(32), 
Space complexity is O(1).
       
