Question:
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, 
then reverse the first k characters and leave the other as original.

Example 1:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Solution:
We will reverse each block of 2k characters directly.
Each block starts at a multiple of 2k: for example, 0, 2k, 4k, 6k, .... One thing to be careful about is we may not reverse each block 
if there aren't enough characters. To reverse a block of characters from i to j, we can swap characters in positions i++ and j--.

class Solution(object):
    def reverseStr(self, s, k):
        a = list(s)
        for i in xrange(0, len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)

