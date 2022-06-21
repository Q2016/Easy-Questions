Question:
Write an algorithm to determine if a number n is happy. A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy. Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1


Solution:
class Solution:
    def isHappy(self, n: int) -> bool:
        
        def squar(n):
            string=str(n)
            tmp=0
            for c in string:
                i=int(c)
                tmp=tmp+i**2
            return tmp
        m=0
        while n!=1 and m<100:
            m+=1
            n=squar(n)     
        return True if n==1 else False
    
There are 2 parts to the algorithm we'll need to design and code.
1)Given a number n, what is its next number?
2)Follow a chain of numbers and detect if we've entered a cycle.
Part 1: can be done by using the division and modulus operators to repeatedly take digits off the number until none remain, 
and then squaring each removed digit and adding them together. 
Part 2: can be done using a HashSet. Each time we generate the next number in the chain, we check if it's already in our HashSet.
If it is not in the HashSet, we should add it.
If it is in the HashSet, that means we're in a cycle and so should return false.

**The reason we use a HashSet and not a Vector, List, or Array is because we're repeatedly checking whether or not numbers are in it. 
Checking if a number is in a HashSet takes O(1) time, whereas for the other data structures it takes O(n) time. Choosing the correct 
data structures is an essential part of solving these problems.
    
    
    
def isHappy(self, n: int) -> bool:

    def get_next(n):
        total_sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            total_sum += digit ** 2
        return total_sum

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)

    return n == 1    



Similar question:
    
The Collatz Conjecture says if you take a positive integer N and repeatedly set either N=N/2 (if it's even) or N=3N+1 (if it's odd), 
N will eventually be 1.
5 -> 16 -> 8 -> 4 -> 2 -> 1 (5 steps).
Given N, how many steps does it take to reach 1?    


Recursive solution with memoization

def  collatz(num, memo={1: 0}):
     if num in memo:
         return memo[num]

    if num % 2:
        res = 1 + collatz(3*num + 1, memo)
    else:
        res = 1 + collatz(num//2, memo)

    memo[num] = res
    return res
