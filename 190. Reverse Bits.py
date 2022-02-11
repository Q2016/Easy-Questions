Question:
Reverse bits of a given 32 bits unsigned integer.
Note:
Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will 
be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation 
is the same, whether it is signed or unsigned. In Java, the compiler represents the signed integers using 2's complement notation. 
Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.
 
Example 1:
Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which 
its binary representation is 00111001011110000010100101000000.

Solution:
We are asked to reverse bits in our number. What is the most logical way to do it? Create number out, process original number bit by bit from end and add this bit to the end of our out number, and that is all! Why it is works?

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
Compexity: time complexity is O(32), space complexity is O(1).

Follow up There is O(5) smart solution which quite impressive, see the most voted post in discussion by @tworuler. We also can hash some 8-bits parts, so we can inverse 4 parts on the fly, with time complexity O(4) and memory complexity O(256) (and preprocessing O(256) as well).

class Solution:
    def reverseBits(self, n):
        out = 0
        for i in range(32):
            out = (out << 1)^(n & 1)
            n >>= 1
        return out
