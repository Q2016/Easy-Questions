Question:
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
Input: s = "aba"
Output: true

  




    
Solution: Two Pointers
  https://www.youtube.com/watch?v=JrxRYBwG6EI
    
Class Solution:
  def validPalindrome(self, s):
    l, r=0, len(s)-1
    
    while l<r:
      if s[l] != s[r]:
        skipL, skipR=s[l+1:r+1], s[l:r]
        return (skipL==skipL[::-1] or skipR==skipR[::-1])
      
      l, r = l+1, r-1
      
      return True
    
Complexity: O(2n)  ~ O(n)
  
  
  
  
  
Approach 2: Recursive  
  
For figure: https://leetcode.com/problems/valid-palindrome-ii/discuss/1452155/Python-Visual-Explanation-Picture-is-worth-a-thousand-words    

1- s is a palindrome - great, we can just return true.

2- Somewhere in s, there will be a pair of mismatched characters. We must use our allowed deletion on one of these characters. 
Try both options - if neither results in a palindrome, then return false. Otherwise, return true. We can "delete" the character at j 
by moving our bounds to (i, j - 1). Likewise, we can "delete" the character at i by moving our bounds to (i + 1, j).



    def validPalindrome(self, s):
        i, j = 0, len(s) - 1
        
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return self.validPalindromeUtil(s, i + 1, j) or self.validPalindromeUtil(s, i, j - 1)
        return True
    
    def validPalindromeUtil(self, s, i, j):
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        
        return True     
      
      
Complexity Analysis

Given N as the length of s,

Time complexity: O(N).

The main while loop we use can iterate up to N / 2 times, since each iteration represents a pair of characters. On any given iteration, 
we may find a mismatch and call checkPalindrome twice. checkPalindrome can also iterate up to N / 2 times, in the worst case where the 
first and last character of s do not match.

Because we are only allowed up to one deletion, the algorithm only considers one mismatch. This means that checkPalindrome will never be 
called more than twice.

As such, we have a time complexity of O(N).

Space complexity: O(1).

The only extra space used is by the two pointers i and j, which can be considered constant relative to the input size.
