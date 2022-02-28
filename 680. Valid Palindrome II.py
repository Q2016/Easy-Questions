Question:
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
Input: s = "aba"
Output: true

    
    
Solution: Recursive
For figure: https://leetcode.com/problems/valid-palindrome-ii/discuss/1452155/Python-Visual-Explanation-Picture-is-worth-a-thousand-words    
    
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
