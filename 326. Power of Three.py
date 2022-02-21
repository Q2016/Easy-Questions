Question:
Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3x.

Solution:
One simple way of finding out if a number n is a power of a number b is to keep dividing n by b as long as the 
remainder is 0. This is because we can write
n = b^x 
n=b×b×…×b
Hence it should be possible to divide n by b x times, every time with a remainder of 0 and the end result to be 1.


def isPowerOfThree(int n) :
    if (n < 1) :
        return false;
    while (n % 3 == 0) :
        n /= 3;
    return n == 1;

