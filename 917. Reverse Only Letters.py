Question:
Given a string s, reverse the string according to the following rules: All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed. Return s after reversing it.

Example 1:
Input: s = "ab-cd"
Output: "dc-ba"

Solution: IS this correct?
Collect the letters of S separately into a stack, so that popping the stack reverses the letters. (Alternatively, we could have collected 
the letters into an array and reversed the array.) Then, when writing the characters of S, any time we need a letter, we use the 
one we have prepared instead.

class Solution(object):
    def reverseOnlyLetters(self, S):
        letters = [c for c in S if c.isalpha()]
        ans = []
        for c in S:
            if c.isalpha():
                ans.append(letters.pop()) # pop from the end of the list
            else:
                ans.append(c)
        return "".join(ans)
