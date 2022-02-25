Question:
Given a string, determine if a permutation of the string could form a palindrome.
For example, "code" -> False, "aab" -> True, "carerac" -> True.





Hint:
Consider the palindromes of odd vs even length. What difference do you notice? Count the frequency of each character. 
If each character occurs even number of times, then it must be a palindrome. How about character which occurs odd number of times?


Complexity of the code below is O(n), we could also use collections.Counter:
Counter is just a subclass of dict. Constructing it is O(n), because it has to iterate over the input, but operations on individual elements remain O(1).    

Solution: Set
class Solution(object):
    def canPermutePalindrome(self, s):

        oddChars = set()
        for c in s:
            if c in oddChars:
                oddChars.remove(c)
            else:
                oddChars.add(c)
        return len(oddChars) <= 1
