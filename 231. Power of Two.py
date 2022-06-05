Question:
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.

















Solution: Bits


class Solution(object):
    def isPowerOfTwo(self, n):
        i=1
        while (i<n):
            i*=2
            
        return i==n
