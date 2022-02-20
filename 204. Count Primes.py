Question:
Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.


Solution:
Animation: https://leetcode.com/problems/count-primes/discuss/1200796/JS-Python-Java-C%2B%2B-or-Easy-Sieve-of-Eratosthenes-Solution-w-Explanation    
    
    
    def countPrimes(self, n: int) -> int:

        if n <= 2:
            return 0
        res = [True] * n
        res[0] = res[1] = False
        for i in range(2, n):
            if res[i] == True:
                for j in range(i, int((n-1)/i+1)):
                    res[i*j] = False
        return sum(res)
