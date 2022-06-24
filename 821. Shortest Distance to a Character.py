Question:
Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and 
answer[i] is the distance from index i to the closest occurrence of character c in s.
The distance between two indices i and j is abs(i - j), where abs is the absolute value function.

Example 1:
Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]


    
    
    
    
    
    
    
    
    
    
    
    
Solution:Min Array (similar to 849. Maximize Distance to Closest Person)
    
For each index S[i], let's try to find the distance to the next character C going left, and going right. 
The answer is the minimum of these two values.
When going left to right, we'll remember the index prev of the last character C we've seen. Then the answer is i - prev.
When going right to left, we'll remember the index prev of the last character C we've seen. Then the answer is prev - i.
We take the minimum of these two answers to create our final answer.

class Solution(object):
    def shortestToChar(self, S, C):
        prev = float('-inf')
        ans = []
        for i, x in enumerate(S):
            if x == C: prev = i
            ans.append(i - prev)

        prev = float('inf')
        for i in xrange(len(S) - 1, -1, -1):
            if S[i] == C: prev = i
            ans[i] = min(ans[i], prev - i)

        return ans

    
    
Complexity Analysis

Time Complexity: O(N), where N is the length of S. We scan through the string twice.

Space Complexity: O(N), the size of ans.    
