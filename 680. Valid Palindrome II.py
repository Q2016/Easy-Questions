Question:
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
Input: s = "aba"
Output: true

Solution:
We can use the standard two-pointer approach that starts at the left and right of the string and move inwards. 
Whenever there is a mismatch, we can either exclude the character at the left or the right pointer. We then take the two 
remaining substrings and compare against its reversed and see if either one is a palindrome.

💯 Check out https://techinterviewhandbook.org for more tips and tricks to ace your technical interview 💯

class Solution(object):
    def validPalindrome(self, s):

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
            left, right = left + 1, right - 1
        return True  
      
      
# Time: O(n)
# Space: O(n)      
