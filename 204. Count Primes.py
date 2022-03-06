Question:
Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

  
  
  
  

Solution:
Animation: https://leetcode.com/problems/count-primes/discuss/1200796/JS-Python-Java-C%2B%2B-or-Easy-Sieve-of-Eratosthenes-Solution-w-Explanation    
  
There are several ways to go about solving this problem, but the classic solution is known as the sieve of Eratosthenes. For the sieve of Eratosthenes, 
we start by creating a boolean array (seen) of size n to represent each of the numbers less than n.
We start at 2 and for each number processed (num), we iterate through and mark each multiple (mult) of num, starting at num^2, as seen. We start at num^2 
because every multiple up to the num'th multiple will have been guaranteed to have been seen before, since they're also a multiple of a smaller number. 
For example, when processing 5s, we can skip to 25 because 10 will have been seen when we processed 2s, 15 when we processed 3s, and 20 when we processed 2s.
Then we move num forward, skipping any numbers that have already been seen. By doing this, we will only stop on prime numbers, because they haven't 
been seen as a multiple of a previous iteration. We just have to update our count (ans) each time we stop and then return ans once we reach n.


    
    def countPrimes(self, n: int) -> int:

        if n <= 2:
            return 0
        res = [True] * n
        res[0] = res[1] = False
        for i in range(2, n):
            if res[i] == True:
                for j in range(i, int((n-1)/i+1)): # look at the index below, (n-1)/i+1 is fixed by num^2 condition mentioned above
                    res[i*j] = False
        return sum(res)
