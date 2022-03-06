Question:
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.

Solution: Bits

The binary form of every power of two likes 0b100...0, because pow(2, n) == 1 << n
1 = 0b1
2 = 0b10
4 = 0b100
8 = 0b1000
...
the binary form of everypow(2, n) - 1 likes0b11..1
1 - 1 = 0 = 0b0        =>  1 & 0 = 0b1    & 0b0    = 0
2 - 1 = 1 = 0b1        =>  2 & 1 = 0b10   & 0b1    = 0
4 - 1 = 3 = 0b11       =>  4 & 3 = 0b100  & 0b11   = 0
8 - 1 = 7 = 0b111      =>  8 & 7 = 0b1000 & 0b111  = 0


class Solution(object):
    def isPowerOfTwo(self, n):
        return n and not (n & n - 1)
