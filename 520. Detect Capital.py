Question:
We define the usage of capitals in a word to be right when one of the following cases holds:
All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

Example 1:
Input: word = "USA"
Output: true

Solution: Regex
Hey, if we want to do pattern matching, why don't we use Regular Expression (Regex)? Regex is a great way to match a given pattern to a string.
The pattern of case 1 in regex is [A-Z]*, where [A-Z] matches one char from 'A' to 'Z', *∗ represents repeat the pattern before it at 
least 0 times. Therefore, this pattern represents "All capital".
The pattern of case 2 in regex is [a-z]*, where similarly, [a-z] matches one char from 'a' to 'z'. Therefore, this pattern represents "All not capital".
Similarly, the pattern of case 3 in regex is [A-Z][a-z]*.
Take these three pattern together, we have [A-Z]*|[a-z]*|[A-Z][a-z]*, where "|" represents "or".
Still, we can combine case 2 and case 3, and we get .[a-z]*, where "." can matches any char.
Therefore, the final pattern is [A-Z]*|.[a-z]*.

import re

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return re.fullmatch(r"[A-Z]*|.[a-z]*", word)
